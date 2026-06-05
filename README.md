# PlayPro UI Automation Framework

## Overview

This project is a UI Automation Testing Framework developed using:

* Python 3.12
* Selenium WebDriver
* Pytest
* Pytest HTML Reports

The framework is designed to automate PlayPro web application testing and supports:

* Cross-browser execution
* Reusable fixtures
* Test parametrization
* Explicit waits
* HTML reporting
* Scalable Page Object Model architecture

## Project Structure

```text
python-automation/
│
├── config/
├── pages/
├── tests/
├── reports/
├── screenshots/
├── utils/
├── conftest.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python -m venv .venv
```

Activate environment:

```bash
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Execute all tests:

```bash
pytest -v
```

Generate HTML report:

```bash
pytest -v --html=reports/report.html
```

## Features

* Selenium WebDriver
* Pytest Fixtures
* Cross Browser Testing
* HTML Reporting
* Explicit Waits
* Page Object Model (POM)
* Easy CI/CD integration

## Author

Chaker Ben Said
QA Automation Engineer

"""
How to  execute pytest tests in cmd command:
  + pytest    
  + pytest tests/play/pro/v3/test_open_page.py
  + pytest tests/play/pro/v3/test_open_page.py -v --html=reports/report.html
  + pytest tests/play/pro/v3/**.py -v --html=reports/report.html
  + @pytest.mark.smoke
    def test_login():
       pass
    Run only the smoke tests :  pytest -m
"""

"""
To implement parameterized cross-browser testing using Pytest and Selenium, you should use a parameterized Pytest fixture inside a conftest.py file. This structural approach isolates the browser setup and cleanup logic from your actual test cases, ensuring that every test automatically runs across all specified browsers.1. Project StructureCreate two files in your test directory:conftest.py: Houses the cross-browser setup fixture.test_suite.py: Contains your Selenium test cases.2. Configure the Shared Fixture (conftest.py)This file defines which browsers to test against. Pytest will spin up a fresh Selenium WebDriver instance for each browser specified in the params list.pythonimport pytest
from selenium import webdriver

# Define the browsers you want to test against
@pytest.fixture(params=["chrome", "firefox", "edge"], scope="function")
def driver(request):
    browser = request.param
    
    # Initialize the appropriate WebDriver instance
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # Add options like headless if needed: options.add_argument("--headless")
        local_driver = webdriver.Chrome(options=options)
        
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        local_driver = webdriver.Firefox(options=options)
        
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        local_driver = webdriver.Edge(options=options)
        
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    # Optional: Maximize window or set timeouts
    local_driver.implicitly_wait(10)
    
    # Provide the driver instance to the test function
    yield local_driver
    
    # Teardown: Safely close the browser session after the test completes
    local_driver.quit()
Utilisez le code avec précaution.3. Write Your Test (test_suite.py)Your test functions accept the driver fixture as an argument. You do not need to manually configure loops or browser conditions inside the test.pythonfrom selenium.webdriver.common.by import By

def test_google_search(driver):
    # Navigate to the target website
    driver.get("https://google.com")
    
    # Validate the page title
    assert "Google" in driver.title
    
    # Example action: Locate search box
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()
Utilisez le code avec précaution.4. Execute the TestsOpen your terminal and execute pytest. Pytest automatically multiplies your tests by the number of browsers listed in your fixture.bash# Run tests sequentially (Will run 3 times: Chrome, Firefox, Edge)
pytest test_suite.py -v
Utilisez le code avec précaution.Speeding Up with Parallel ExecutionRunning cross-browser tests sequentially can become incredibly slow. You can distribute the parameterized browser sessions simultaneously across multiple CPU cores by utilizing the pytest-xdist plugin.bash# Install the parallel execution plugin
pip install pytest-xdist

# Run all browser instances concurrently
pytest test_suite.py -n 3 -v
"""