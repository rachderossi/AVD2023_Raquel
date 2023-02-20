from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time


s = Service('/Users/raquelrossi/Downloads/chromedriver')
browser = webdriver.Chrome(service=s)
browser.get("https://www.gutenberg.org/ebooks/author/6699")

browser.find_elements(By.CLASS_NAME, 'booklink')[19].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[1].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[2].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[3].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[4].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[5].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[6].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[7].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[8].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[9].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[10].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[11].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[12].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[13].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[14].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[15].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[16].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[17].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[18].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[0].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[20].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[21].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[22].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[23].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[24].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

#browser.find_elements(By.CLASS_NAME, 'booklink')[0].click()
# browser.find_element(
#    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
#browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[1].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[2].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[3].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[4].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[5].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[6].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[7].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[8].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

#browser.find_elements(By.CLASS_NAME, 'booklink')[9].click()
# browser.find_element(
#   By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
#browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[10].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[11].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[12].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[13].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[14].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[15].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[16].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[17].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[18].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[19].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[20].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[21].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[22].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[23].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[24].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()
time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=51"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[0].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()
time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=51"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[1].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()
time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=51"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[2].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()

time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=26"]').click()
time.sleep(5)
browser.find_element(
    By.CSS_SELECTOR, '[href="/ebooks/author/6699?start_index=51"]').click()

browser.find_elements(By.CLASS_NAME, 'booklink')[3].click()
browser.find_element(
    By.CSS_SELECTOR, '[type="application/x-mobipocket-ebook"]').click()
browser.find_element(By.CSS_SELECTOR, '[href="/ebooks/author/6699"]').click()
time.sleep(7)

browser.quit()
