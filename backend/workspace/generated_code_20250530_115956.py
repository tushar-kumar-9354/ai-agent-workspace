from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_website(url, word_count=1000):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    text = ""
    start_time = time.time()
    while len(text.split()) < word_count and time.time() - start_time < 60:
        try:
            elements = driver.find_elements(By.XPATH, "//*[self::p or self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6 or self::span or self::div or self::article]")
            for element in elements:
                if element.is_displayed():
                    text += element.text + " "
            time.sleep(1)

            
            try:
                next_button = driver.find_element(By.XPATH, "//a[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'next')]")
                if next_button.is_displayed() and next_button.is_enabled():
                   
                    next_button.click()
                    time.sleep(2)
                else:
                    break
            except:
                 pass


        except Exception as e:
            print(f"Error extracting text: {e}")
            break

    driver.quit()
    words = text.split()
    if len(words) > word_count:
       text = " ".join(words[:word_count])
    else:
        text = " ".join(words)
    return text

if __name__ == '__main__':
    website_url = "https://www.example.com"  
    scraped_text = scrape_website(website_url)

    print(scraped_text)
import json

with open("hn_articles.json", "w") as f:
    json.dump(scraped_text, f, indent=4)
