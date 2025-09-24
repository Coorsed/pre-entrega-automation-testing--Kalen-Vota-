

# --- Imports ---

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import *


# --- Configuration of the driver ---

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# --- Configuration of the explicit wait ---

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


# --- Test Steps ---

def test_login(driver,wait):

    """
    --------- Login test ---------
    Verify that users can login with valid username/password and enter in /inventory site
    """

    # Open the website 
    driver.get("https://www.saucedemo.com")

    # input user name
    try:
        wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    except:
        print("❌ Website not opened")
    print("✅ Saucedemo website opened")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    assert driver.find_element(By.ID, "user-name").get_attribute("value") == "standard_user", "❌ Failed user input"
    print("✅ Succesful input user")

    #input password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    assert driver.find_element(By.ID, "password").get_attribute("value") == "secret_sauce", "❌ Failed password input"
    print("✅ Succesful input password")

    #click on login
    driver.find_element(By.ID, "login-button").click()

    #wait to redirection
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
    except: 
        print("❌ Fail page load or incorrect url")
    print("✅ Inventory page loaded")

    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "❌ Redirection failed"
    print("✅ Successful redirection")

    assert driver.title == "Swag Labs", "❌ Title is NOT correct"
    print("✅ Title:", driver.title)

    print(" --------- ✅ Test OK ✅ --------- ")



def test_inventory(driver):

    """
    --------- Inventory Page test ---------
    Function: verify that the title is OK, that there is at least one product, and the interface elementes are present.
    """

    #auto-login
    auto_login(driver)

    #Verify the title
    assert driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text == "Products", "❌ Products title is NOT correct"
    print("✅ Products title is correct")

    #Verify products existens
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) >=1, "❌ No products found"
    print("✅ There is at least one product")

    #Save price and name of the first product
    try:
        first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    except:
        first_product_name = "❌ Name not found"
    print(f"\t▶️  First product name is: {first_product_name}")

    try:
        first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    except: 
        first_product_price = "❌ Price not found"
    print(f"\t▶️  First product price is: {first_product_price}")

    #Verify interface elements
    assert driver.find_element(By.ID, "shopping_cart_container").is_displayed(), "❌ Cart icon is NOT visible"
    print("✅ Cart icon is visible")

    assert driver.find_element(By.CLASS_NAME, "select_container").is_displayed(), "❌ Filter is NOT visible"
    print("✅ Filter is visible")

    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed(), "❌ Menu is NOT visible"
    print("✅ Menu is visible")

    print(" --------- ✅ Test OK ✅ --------- ")

def test_cart(driver,wait):
    # --------- Add to Cart ---------

    #auto login + auto inventory + first product
    auto_inventory(driver)
    first_product_name, first_product_price = auto_inventory(driver)

    #add to cart
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    try:
        wait.until(EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
    except:
        print("❌ Fail to add to cart")

    print("✅ First product added to cart")

    #Cart number
    try:
        badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
    except:
        print("❌ Cart badge is NOT visible")

    print("✅ Cart badge is visible")

    assert badge.text == "1", print("❌ Cart count is NOT correct")
    print("✅ Cart count is correct")

    # --------- Cart Check ---------

    #cart redirection
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    try:
        wait.until(EC.url_to_be("https://www.saucedemo.com/cart.html"))
    except:
        print("❌ Unsuccesful redirection to cart")

    print("✅ Succesful redirection to Cart page")

    #check cart item is the same as we added
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1, print("❌ There is an incorrect quantity of items in the cart")
    print("✅ There is one item in the cart")

    assert cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text == first_product_name, print("❌ The item in the cart is NOT the correct one")
    print("✅ There is one item in the cart and its the correct one")

    assert driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1", print("❌ The quantity is NOT correct")
    print("✅ The quantity is correct")

    assert driver.find_element(By.CLASS_NAME, "inventory_item_price").text == first_product_price, print("❌ The price is NOT correct")
    print("✅ The price is correct")
        
    print(" --------- ✅ Test OK ✅ --------- \n")
    print(" --------- Test ended --------- ")
