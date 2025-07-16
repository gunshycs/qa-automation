from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login():
  driver = webdriver.Chrome()

  try:
    #Open Orange login page
    driver.get("https://opensource-demo.orangehrmlive.com")

    #Wait for username field to be visible
    WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.NAME, "username"))
    ).send_keys("notAdmin")

    #Wait for password field to be visible
    WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.NAME, "password"))
    ).send_keys("admin321")

    #Wait for login button and click it
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    ).click()

    # Wait for the welcome message after login
    error_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.oxd-alert-content-text"))
    ).text

    assert "Invalid credentials" in error_text, "❌ Test Failed: Expected error not found"
    print("✅ Test Passed: Invalid login shows correct error")
  finally:
    driver.quit()

if __name__ == "__main__":
  test_invalid_login()
