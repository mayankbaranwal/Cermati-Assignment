from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Download Chrome webdriver automatically according to latest browser version!
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(60)

driver.implicitly_wait(30)
driver.get("https://www.ebay.com/")
driver.maximize_window()
try:
    driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search for anything')]").send_keys('Macbook')
    dropdown = Select(driver.find_element(By.XPATH, "//select[@aria-label = 'Select a category for search']"))
    dropdown.select_by_visible_text('Computers/Tablets & Networking')
    driver.find_element(By.CSS_SELECTOR, '#gh-btn').click()

    # check if Page Loads Completely
    driver.execute_script("window.scrollBy(0,17000)", "")
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    pageLoadText = driver.find_element(By.CSS_SELECTOR, "#srp-ipp-label-text").text
    assert 'Items Per' in pageLoadText

    # Checking the first result contains the Searched Keyword (MacBook) in the string
    firstResultContent = driver.find_element(By.XPATH,
                                             "//ul[@class='srp-results srp-list clearfix']/descendant::li[23]").text
    print(firstResultContent)
    assert 'Macbook' in firstResultContent
except TimeoutException:
    print("Timed out waiting for page to load!")
finally:
    # Close the WebDriver
    driver.quit()
