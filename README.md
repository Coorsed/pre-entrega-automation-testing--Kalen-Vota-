

# ⚡Pre-submission Final Project - Testing Automation

In this project we apply **Python** and **Selenium WebDriver** to test  **SauceDemo** website.

## 🎯 Objective

This project automates repetitive tests to save time and resources, optimizing the following workflow:
- Login with valid and invalid credentials
- Verify the product catalog
- Interact with the cart: add products and verify content

## 🛠️ Technologies Used

- **Python**: Main programming language  
- **Pytest**: Testing framework to execute tests  
- **Selenium WebDriver**: Automates the web interface  
- **Git/GitHub**: Code sharing and version control  

## 📁 Project Structure
```text
📁 pre_entrega/
├──📁 reports/                          # Reports folder (auto-created)
│   │
│   ├──📁 run_2025-09-25_19-12-34       # (Example) Test run with fail
│   │   ├── 📄 report.html              # Test report
│   │   └── 📸 test_cart_2025-09-25.png # Screenshot of the fail
│   │
│   └──📁 run_2025-09-25_19-13-11       # (Example) Test run without fail
│       └── 📄 report.html              # Test report
│
├──📁 tests                             # Folder for test cases
│   ├── 📄 __init__.py                  # Convert the folder into a package
│   ├── 📄 conftest.py                  # Loads shared fixtures from utils/conftest.py
│   ├── 📄 console-test_saucedemo.py    # Run test only with Selenium, results in console
│   └── 📄 test_saucedemo.py            # Run test with pytest
│
├──📁 utils/                            # Helpers to avoid code repetition
│   ├── 📄 __init__.py                  # Convert the folder into a package
│   ├── 📄 conftest.py                  # Pytest configuration
│   └── 📄 helpers.py                   # Reusable functions
│
├📄 pytest.ini                          # Pytest launch options
└📄 README.md                           # You are here 📌
```
## ⚙️ Dependencies Installation

- Install Python 3.x or newer.

Install dependencies:
```
pip install selenium pytest pytest-html
```

- Download the correct WebDriver:

- ChromeDriver (for Chrome)

- GeckoDriver (for Firefox)

## ▶️ To run the tests and generate a report, execute:
```
python -m pytest -v
```
## ✅ Test Functions

▶️ Automated login

- With valid credentials

▶️ Catalog verification

- Page title

- Products verification

- Check page elements

▶️ Cart verification

- Add products

- Verify cart badge

- Navigate to cart

- Verify the product

## ✨ Additional Features

- Auto-screenshots: If a test fails, Selenium takes a screenshot of the page.

- Reusable functions are stored in helpers.py.

## 👤 Author: Kalen Vota

## 📝 Notes
This project was designed using the SauceDemo version available in September 2025.