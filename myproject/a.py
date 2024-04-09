import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service
def crawl_shopee_products(keyword, num_pages=1):
    products = []
    print("111111111111111111")
    # Setting up the Chrome WebDriver
    service = Service('C:\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    print("111111111111111111")
    for page in range(1, num_pages + 1):
        url = f"https://shopee.com.my/search?keyword={keyword}&page={page}"
        driver.get(url)
        time.sleep(3)  # Give some time for the page to load

        # Find product items
        product_items = driver.find_elements(By.CLASS_NAME, "col-xs-2-4.shopee-search-item-result__item")
        for item in product_items:
            product = {}
            product["name"] = item.find_element(By.CLASS_NAME, "_1NoI8_").text.strip()
            product["price"] = item.find_element(By.CLASS_NAME, "_1xk7ak").text.strip()
            product["image_url"] = item.find_element(By.TAG_NAME, "img").get_attribute("src")
            products.append(product)

    driver.quit()  # Close the WebDriver
    return products

# Example usage
keyword = "laptop"
num_pages = 3
products = crawl_shopee_products(keyword, num_pages)

# Convert products to DataFrame
df = pd.DataFrame(products)

# Save DataFrame to CSV
df.to_csv("shopee_products.csv", index=False)
