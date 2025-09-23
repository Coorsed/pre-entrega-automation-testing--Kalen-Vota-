# --- Imports ---
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

# --- Test Steps ---

    # --- login automation---

def test_login(driver):

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com")
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    assert driver.find_element(By.ID, "user-name").get_attribute("value") == "standard_user"

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    assert driver.find_element(By.ID, "password").get_attribute("value") == "secret_sauce"

    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert driver.title == "Swag Labs"


    # --- Inventory page ---
def test_inventory_page(driver):
    test_login(driver)
    assert driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text == "Products"   
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) >=1

    first_product = products[0]
    first_product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert driver.find_element(By.ID, "shopping_cart_container").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "select_container").is_displayed()
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()

    return first_product_name, first_product_price

    # --- add to cart ---
def test_add_to_cart(driver):
    test_inventory_page(driver)
    wait = WebDriverWait(driver, 10)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed()

    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
    assert badge.is_displayed() 
    print("hola")
    assert badge.text == "1"


    # --- cart check ---

def test_cart_check(driver, first_product_name, first_product_price):
    test_add_to_cart(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"   

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1   
    first_cart_item = cart_items[0]
    assert  first_cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text == first_product_name
    assert driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1"
    assert driver.find_element(By.CLASS_NAME, "inventory_item_price").text == first_product_price
