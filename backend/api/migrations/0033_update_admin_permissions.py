from django.db import migrations
from django.db.migrations import RunPython


def update_permissions(apps, schema_editor):
    """
    Updates the permissions and removes the create/edit fuel suppliers
    from Government Analyst and Director roles
    """
    db_alias = schema_editor.connection.alias

    permission = apps.get_model("api", "Permission")
    role = apps.get_model("api", "Role")
    role_permission = apps.get_model("api", "RolePermission")

    permission.objects.using(db_alias).create(
        code='EDIT_FUEL_SUPPLIER_USERS',
        name="Edit Fuel Supplier Users' Information"
    )

    role_permission.objects.using(db_alias).bulk_create([
        role_permission(
            role=role.objects.using(db_alias).get(name='Admin'),
            permission=permission.objects.using(db_alias).get(
                code='EDIT_FUEL_SUPPLIER_USERS')
        ),
        role_permission(
            role=role.objects.using(db_alias).get(name='Admin'),
            permission=permission.objects.using(db_alias).get(
                code='VIEW_APPROVED_CREDIT_TRANSFERS')
        ),
        role_permission(
            role=role.objects.using(db_alias).get(name='Admin'),
            permission=permission.objects.using(db_alias).get(
                code='VIEW_CREDIT_TRANSFERS')
        ),
        role_permission(
            role=role.objects.using(db_alias).get(name='Admin'),
            permission=permission.objects.using(db_alias).get(
                code='VIEW_FUEL_SUPPLIERS')
        )
    ])


def revert_permissions(apps, schema_editor):
    """
    Reverts the permission back to its previous state by assigning
    back the permission back to Government Analyst and Director
    """
    db_alias = schema_editor.connection.alias

    permission = apps.get_model("api", "Permission")
    role_permission = apps.get_model("api", "RolePermission")

    role_permission.objects.using(db_alias).filter(
        permission__code__in=[
            "EDIT_FUEL_SUPPLIER_USERS",
            "VIEW_APPROVED_CREDIT_TRANSFERS",
            "VIEW_CREDIT_TRANSFERS",
            "VIEW_FUEL_SUPPLIERS"
        ],
        role__name="Admin").delete()

    permission.objects.using(db_alias).filter(
        code="EDIT_FUEL_SUPPLIER_USERS"
    ).delete()


class Migration(migrations.Migration):
    """
    Attaches the functions for the migrations
    """
    dependencies = [
        ('api', '0032_role_rename'),
    ]

    operations = [
        RunPython(update_permissions, revert_permissions)
    ]
