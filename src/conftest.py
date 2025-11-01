import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import datetime

GRID_URL = "http://localhost:4444/wd/hub"

@pytest.fixture(params=["chrome", "firefox"])
def setup_driver(request):
    browser = request.param
    print(f"🌍 Starting test on {browser.upper()} via Selenium Grid")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_page_load_timeout(30)
    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("src/reports/screenshots", exist_ok=True)
        path = f"src/reports/screenshots/{request.node.name}_{browser}_{ts}.png"
        driver.save_screenshot(path)
        print(f"📸 Screenshot saved to {path}")

    driver.quit()
    print(f"✅ Closed {browser.upper()} session.")
