

# --- Imports ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --- Configuration of the driver ---

options = Options()
options.add_argument("--log-level=3")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)


# --- Test Steps ---

try:

    # --- login ---

    print()
    print(" --------- Login --------- ")

    driver.get("https://www.saucedemo.com")
    if driver.current_url == "https://www.saucedemo.com/":
        print("✅ Website opened")
    else:
        print("❌ Website not opened")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    if driver.find_element(By.ID, "user-name").get_attribute("value") == "standard_user":
        print("✅ Succesful input user")
    else:
        print("❌ Unsuccesful input user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    if driver.find_element(By.ID, "password").get_attribute("value") == "secret_sauce":
        print("✅ Succesful input password")
    else:
        print("❌ Unsuccesful input password")

    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    if driver.current_url == "https://www.saucedemo.com/inventory.html":
        print("✅ Succesful login")
        print("✅ Successful redirection")
    else:
        print("❌ Unsuccesful login")

    if driver.title == "Swag Labs":
        print("✅ Title:", driver.title)
    else:
        print("❌ Wrong title:", driver.title)

    print(" --------- Test OK --------- \n")


    # --- Inventory page ---

    print(" --------- Inventory Page --------- ")

    if driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text == "Products":        
        print("✅ Products title is correct")
    else:
        print("❌ Products title is NOT correct") 

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    if len(products) >=1:
        print("✅ There is at least one product")
        first_product = products[0]
        print("\t▶️  First product name is:", first_product.find_element(By.CLASS_NAME, "inventory_item_name").text)
        first_product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
        print("\t▶️  First product price is:", first_product.find_element(By.CLASS_NAME, "inventory_item_price").text)
        first_product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
    else:
        print("❌ There is NO product")
    
    if driver.find_element(By.ID, "shopping_cart_container").is_displayed():
        print("✅ Cart icon is visible")
    else:
        print("❌ Cart icon is NOT visible")

    if driver.find_element(By.CLASS_NAME, "select_container").is_displayed():
        print("✅ Filter is visible")
    else:
        print("❌ Filter is NOT visible")

    if driver.find_element(By.ID, "react-burger-menu-btn").is_displayed():
        print("✅ Menu is visible")
    else:
        print("❌ Menu is NOT visible")

    print(" --------- Test OK --------- \n")


    # --- add to cart ---

    print(" --------- Add to Cart --------- ")

    first_product.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    if first_product.find_element(By.ID, "remove-sauce-labs-backpack").is_displayed():
        print("✅ First product added to cart")
    else:
        print("❌ First product NOT added to cart")

    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
    if badge.is_displayed():
        print("✅ Cart badge is visible")
    else:
        print("❌ Cart badge is NOT visible")  

    if badge.text == "1":
        print("✅ Cart count is correct")
    else:
        print("❌ Cart count is NOT correct")

    print(" --------- Test OK --------- \n")


    # --- cart check ---

    print(" --------- Cart Check --------- ")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    if driver.current_url == "https://www.saucedemo.com/cart.html":     
        print("✅ Succesful redirection to cart")
    else:
        print("❌ Unsuccesful redirection to cart")
        
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    if len(cart_items) == 1:
        print("✅ There is one item in the cart")
        first_cart_item = cart_items[0]
        if  first_cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text == first_product_name:
            print("✅ There is one item in the cart and its the correct one")
        else:
            print("❌ The item in the cart is NOT the correct one")

        if driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1":
            print("✅ The quantity is correct")
        else:
            print("❌ The quantity is NOT correct")

        if driver.find_element(By.CLASS_NAME, "inventory_item_price").text == first_product_price:
            print("✅ The price is correct")
        else:
            print("❌ The price is NOT correct")
        
    else:
        print("❌ There is NOT one item in the cart")
    print(" --------- Test OK --------- \n")


finally:
    print(" --------- Test ended --------- \n")
    driver.quit()