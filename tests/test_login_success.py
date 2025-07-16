from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    driver = webdriver.Chrome()

    try:
        # Open OrangeHRM login page
        driver.get("https://opensource-demo.orangehrmlive.com")

        # Wait for username field to be visible (max 10 seconds)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys("Admin")

        # Wait for password field and send keys
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        ).send_keys("admin123")

        # Wait for Login button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
        ).click()

        # Wait for the welcome message after login
        welcome_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.oxd-userdropdown-name"))
        ).text

        assert "Paul Collings" in welcome_text or "Admin" in welcome_text, "Login failed!"
        print("✅ Test Passed: Successful login")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
