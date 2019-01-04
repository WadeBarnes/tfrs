import requests
from tfrs.settings import KEYCLOAK


def get_token():
    token_url = '{keycloak}/auth/realms/{realm}/protocol/openid-connect/token'.format(
        keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
        realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'])

    response = requests.post(token_url,
                             auth=(KEYCLOAK['SERVICE_ACCOUNT_CLIENT_ID'],
                                   KEYCLOAK['SERVICE_ACCOUNT_CLIENT_SECRET']),
                             data={'grant_type': 'client_credentials'})

    token = response.json()['access_token']

    return token


def list_users(token):
    users_url = '{keycloak}/auth/admin/realms/{realm}/users'.format(
        keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
        realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'])

    headers = {'Authorization': 'Bearer {}'.format(token)}

    response = requests.get(users_url,
                            headers=headers)

    all_users = response.json()
    for user in all_users:
        users_detail_url = '{keycloak}/auth/admin/realms/{realm}/users/{user_id}/federated-identity'.format(
            keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
            realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'],
            user_id=user['id'])

        response = requests.get(users_detail_url,
                                headers=headers)

    if response.status_code != 200:
        raise RuntimeError('bad response code: {}'.format(response.status_code))


def associate_federated_identity_with_user(token, id, provider, username):
    users_url = '{keycloak}/auth/admin/realms/{realm}/users/{user_id}/federated-identity/{provider}'.format(
        keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
        realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'],
        user_id=id,
        provider=provider)

    headers = {'Authorization': 'Bearer {}'.format(token)}

    data = {
        'userName': username
    }

    response = requests.post(users_url,
                             headers=headers,
                             json=data)


def map_user(keycloak_user_id, tfrs_user_id):

    users_url = '{keycloak}/auth/admin/realms/{realm}/users/{user_id}'.format(
        keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
        realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'],
        user_id=keycloak_user_id)

    headers = {'Authorization': 'Bearer {}'.format(get_token())}

    data = {
        'attributes': {
            'user_id': tfrs_user_id
        }
    }

    response = requests.put(
        users_url,
        headers=headers,
        json=data
    )

    if response.status_code not in [200, 201, 204]:
        raise RuntimeError('bad response code: {}'.format(response.status_code))


def create_user(token, user_name, maps_to_id):
    users_url = '{keycloak}/auth/admin/realms/{realm}/users'.format(
        keycloak=KEYCLOAK['SERVICE_ACCOUNT_KEYCLOAK_API_BASE'],
        realm=KEYCLOAK['SERVICE_ACCOUNT_REALM'])

    headers = {'Authorization': 'Bearer {}'.format(token)}

    data = {
        'enabled': True,
        'username': user_name,
        'attributes': {
            'user_id': maps_to_id
        }
    }

    response = requests.post(users_url,
                             headers=headers,
                             json=data)

    if response.status_code != 204:
        raise RuntimeError('bad response code: {}'.format(response.status_code))

    created_user_response = requests.get(response.headers['Location'], headers=headers)

    return created_user_response.json()['id']

