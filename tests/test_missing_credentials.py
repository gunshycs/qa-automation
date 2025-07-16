from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_missing_cred():
  driver = webdriver.Chrome()

  try:
    # Open OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com")

    # Wait for Login button and click it
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    ).click()

    missing_cred_text = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.oxd-input-field-error-message'))
    ).text

    assert "Required" in missing_cred_text, "❌ Test Failed: Expected error not found"
    print("✅ Test Passed: Missing credentials shows correct error")
  finally:
    driver.quit()

if __name__ == '__main__':
  test_missing_cred()
