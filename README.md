# QA Automation Suite for OrangeHRM Demo

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43a047?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![ChromeDriver](https://img.shields.io/badge/ChromeDriver-White?logo=googlechrome&logoColor=blue)](https://chromedriver.chromium.org/)
[![pytest](https://img.shields.io/badge/Pytest-Testing-blueviolet?logo=pytest&logoColor=white)](https://docs.pytest.org/)

## Overview

This project is a beginner-friendly automated testing suite for the [OrangeHRM demo web app](https://opensource-demo.orangehrmlive.com).  
Built with Python and Selenium WebDriver, it covers core QA automation skills including functional UI testing, error handling, and workflow validation.  

---

## Features

- ✅ Successful login test  
- ✅ Invalid login test with error validation  
- ✅ Missing credentials test  
- *(More tests to be added… logout, UI checks, etc.)*

---

## Technologies Used

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43a047?logo=selenium&logoColor=white)](https://www.selenium.dev/)  
[![ChromeDriver](https://img.shields.io/badge/ChromeDriver-White?logo=googlechrome&logoColor=blue)](https://chromedriver.chromium.org/)  
[![pytest](https://img.shields.io/badge/Pytest-Testing-blueviolet?logo=pytest&logoColor=white)](https://docs.pytest.org/)

---

## Setup Instructions

1. **Clone the repo:**  
   ```bash
   git clone https://github.com/yourusername/qa-automation.git
   cd qa-automation
   
2. **Create & activate a virtual environment:**  
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # macOS/Linux
3. **Intall Dependencies:**
   ```bash
   pip install -r requirments.txt

 5. ***Ensure ChromeDriver is installed and in your PATH:***
   - Download the matching ChromeDriver version from https://chromedriver.chromium.org/downloads and add it to your system PATH or place it in the drivers/ folder.
  
## Running Tests
Run Individual tests with:
```bash
python tests/[name of test].py

   
