import requests
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

API_BASE = "https://jsonplaceholder.typicode.com"

def test_login_with_api_verification(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    inventory = InventoryPage(driver)

    # API Init Step
    user_data = requests.get(f"{API_BASE}/users/1").json()
    assert user_data["id"] == 1
    print(f"✅ API init verified user: {user_data['username']}")

    # UI Step
    login_page.open_login_page()
    login_page.login("standard_user", "secret_sauce")
    assert inventory.is_loaded(), "Inventory page not loaded"

    # API Verification Step
    session_check = requests.get(f"{API_BASE}/posts?userId={user_data['id']}")
    assert session_check.status_code == 200
    print(f"✅ API verification passed for user ID: {user_data['id']}")
