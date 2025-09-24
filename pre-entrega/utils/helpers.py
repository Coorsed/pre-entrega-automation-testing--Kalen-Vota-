

# --- Imports ---
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#CREAR FUNCION PARA HACER LOGIN AUTOMATICO
def auto_login(driver):
    
    driver.get("https://www.saucedemo.com")
    WebDriverWait(driver, 10).until( EC.url_matches("https://www.saucedemo.com"))

    # input user name
    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    #input password
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    #click on login
    driver.find_element(By.ID, "login-button").click()

    #wait to redirection
    WebDriverWait(driver, 10).until( EC.url_contains("inventory.html"))

def auto_inventory(driver):

    #auto-login
    auto_login(driver)

    #Verify products existens
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    return first_product_name, first_product_price