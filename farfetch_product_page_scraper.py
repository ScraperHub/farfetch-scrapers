from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import csv

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

# Function to scrape details from a product page using Crawlbase
def scrape_product_page(url):
    options = {
        "ajax_wait": "true",  # Wait for JavaScript rendering
        "page_wait": "3000"   # Wait 3 seconds for the page to fully load
    }
    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':
        soup = BeautifulSoup(response['body'], "html.parser")

        # Extract product details
        blurb = soup.select_one('p[data-testid="product-short-description"]').text.strip() if soup.select_one('p[data-testid="product-short-description"]') else "N/A"
        brand = soup.select_one('a[data-component="LinkGhostDark"]').text.strip() if soup.select_one('a[data-component="LinkGhostDark"]') else "N/A"
        price = soup.select_one('div#price').text.strip() if soup.select_one('div#price') else "N/A"
        description = soup.select_one('div[data-testid="product-information-accordion"] div[data-component="AccordionPanel"]').text.strip() if soup.select_one('div[data-testid="product-information-accordion"] div[data-component="AccordionPanel"]') else "N/A"

        return {
            "blurb": blurb,
            "brand": brand,
            "price": price,
            "description": description
        }
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return None

# Function to save product data to a CSV file
def save_product_to_csv(product_data, filename="farfetch_product_details.csv"):
    keys = product_data.keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerow(product_data)

    print(f"Product data saved to {filename}")

# Example usage
product_url = "https://www.farfetch.com/shopping/men/sneakers-product-12345.aspx"
product_details = scrape_product_page(product_url)

if product_details:
    save_product_to_csv(product_details)