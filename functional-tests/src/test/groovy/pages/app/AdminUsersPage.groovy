package pages

import org.openqa.selenium.Keys

class AdminUsersPage extends BaseAppPage {
  static at = { isReactReady() && pageTitle.text() == 'Users' }
  static url = '/admin/users'
  static content = {
    pageTitle { $('#main .page_users h1') }

    // TODO add selector for button carat to select 'Add Fuel Supplier User'?
    newUserButton { $('#new-user') }

    usersTable(wait:true) { $('.ReactTable') }
  }

  void clickNewUserButton() {
    newUserButton.click()
  }

  void setUserNameFilter(String usersName) {
    // Get the filters header row, and get the input field of its first child (first column).
    usersTable.$('.-filters').$('.rt-th')[0].$('input').value(usersName)
  }

  void clickUserRow(String usersName) {
    setUserNameFilter(usersName)
    usersTable.$('.rt-tbody').$('.clickable').has('.col-name', text:usersName).click()
  }

  void clickNewFuelSupplierUserButton() {
    newUserButton.siblings('button').click()
    interact {
      waitFor {
        // Wait for the dropdown to populate and click it
        moveToElement(newUserButton.siblings('.dropdown-menu')).click()
      }
    }
  }
}
