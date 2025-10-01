

# --- Imports ---

import pytest
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



# --- Global configuration of driver ---

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()



# --- Configuration of explicit wait ---

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)



# --- Configuration run_dir ---

@pytest.fixture
def run_dir(request):
    return getattr(request.config, "run_report_dir", None)



# --- Configuration of reports ---

def pytest_configure(config):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # --- Search /reports ---
    reports_dir = os.path.join(base_dir, "pre_entrega", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    # --- Create report folder per run ---
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_dir = os.path.join(reports_dir, f"run_{timestamp}")
    os.makedirs(run_dir, exist_ok=True)

    # --- Mod report ---
    report_file = os.path.join(run_dir, "report.html")
    config.option.htmlpath = report_file
    config.option.self_contained_html = True

    # --- Save path ---
    config.run_report_dir = run_dir



# --- Screenshot implementation ---

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        run_dir = getattr(item.config, "run_report_dir", None)

        if driver and run_dir:
            # --- Save screenshot with report.html ---
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(run_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved: {screenshot_path}")