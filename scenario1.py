# Scenario 1: Access a Product via category after applying multiple filters
# o Go to ebay.com
# o Navigate to Search by category > Electronics > Cell Phones & accessories
# o After the page loads, click Cell Phones & Smartphones in the left hand side navigation section.
# o Now, click – All Filters (appears at the end of the filter drop downs)
# o Add 3 filters - Condition, Price and Item location appearing in the pop-up and click apply.
# o Verify that the filter tags are applied.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Download Chrome webdriver automatically according to latest browser version!
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(60)

# opening the website
driver.get("https://www.ebay.com/")
driver.maximize_window()

# Navigate to Search by category > Electronics > Cell Phones & accessories
driver.find_element(By.XPATH, "//button[@id='gh-shop-a']").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Cell phones & accessories')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Cell Phones & Smartphones')]").click()
driver.execute_script("window.scrollBy(0,500)", "")

# Click All Filters Button
element = driver.find_element(By.XPATH, "//button[@aria-label='All Filters']")
driver.execute_script("arguments[0].click();", element)

# Select the 'Price' Filter and send the Price range value filters
driver.find_element(By.XPATH, "//div[@data-aspecttitle='price']").click()
minmaxValues = driver.find_elements(By.XPATH, "//div[@id = 'c3-subPanel-_x-price-textrange']/div/div/div/input")
for i in range(len(minmaxValues)):
    if i == 0:
        minmaxValues[i].send_keys(500)
    else:
        minmaxValues[i].send_keys(2000)

# Select the 'Item Condition' Filter and select the 3 different checkboxes
driver.find_element(By.XPATH, "//div[@data-aspecttitle='LH_ItemCondition']").click()
checkboxes = driver.find_elements(By.XPATH, "//span[@class='field']/span")
for i in range(len(checkboxes)):
    if i == 0 or i == 2 or i == 6:
        checkboxes[i].click()

# Select the 'Item Location' Filter and select the radio button for the US Location
driver.find_element(By.XPATH, "//span[text()='Item Location']").click()
radioBoxes = driver.find_elements(By.XPATH,
                                  "//span[@class = 'radio field__control rbx x-refine__single-select-radio']")
radioBoxes[1].click()

# Apply all the filters with Apply Button
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Apply']")))
driver.find_element(By.XPATH, "//button[@aria-label='Apply']").click()

# Check for the text comes after applying the above 3 filters as search result to validate if we get the result as
# per the applied filters.
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='b-pageheader__text']")))

itemsFound = driver.find_element(By.XPATH, "//span[@class='b-pageheader__text']").text

assert "Cell Phones & Smartphones" in itemsFound
