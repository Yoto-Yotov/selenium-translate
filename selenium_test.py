from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

prefs = {
    "translate_whitelists": {"de": "en"},
    "translate": {"enabled": "true"}
}

options = Options()
options.headless = False
options.add_argument('--no-sandbox')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-infobars')
options.add_argument("--lang=en")

# Add the prefs option to you options to auto-translate
options.add_experimental_option("prefs", prefs)

# Path to your chrome driver
chromedriver = "/home/yoto/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver, options=options)

driver.get('https://www.spiegel.de/politik/deutschland/berlin-bettina-jarasch-wird-ueberraschend-spitzenkandidatin-fuer-berliner-gruenen-a-639b2281-e668-4bea-a91a-d21452abf6cf')

# Find iframe and switch to it
WebDriverWait(driver, 10).until(expected_conditions.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[contains(@id, 'sp_message_iframe')]")))
# Find element in iframe and click it
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div[3]/div[2]/button"))).click()
# Switch back to default content or selenium throws selenium.common.exceptions.WebDriverException: Message: target frame detached
driver.switch_to.default_content()
driver.implicitly_wait(5)
# Get element with text from article and print it's innerHTML
element = driver.find_element_by_xpath('//*[@id="Inhalt"]/article/header/div/div/div[1]/font/font[1]')
print(element.get_attribute('innerHTML'))

print("Done")
