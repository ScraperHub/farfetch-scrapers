from crawlbase import CrawlingAPI
from bs4 import BeautifulSoup
import csv

# Initialize Crawlbase API with your access token
crawling_api = CrawlingAPI({'token': 'YOUR_CRAWLBASE_TOKEN'})

# Function to scrape Farfetch search listings
def scrape_farfetch_listings(url):
    options = {
        'ajax_wait': 'true',  # Wait for JavaScript to load
        'page_wait': '5000'   # Wait 5 seconds for the page to load
    }
    response = crawling_api.get(url, options)

    if response['headers']['pc_status'] == '200':  # Check Crawlbase status
        soup = BeautifulSoup(response['body'].decode('utf-8'), "html.parser")
        products = []

        # Extract product details
        for item in soup.select('ul#catalog-grid > li[data-testid="productCard"]'):
            brand = item.select_one('p[data-component="ProductCardBrandName"]').text.strip() if item.select_one('p[data-component="ProductCardBrandName"]') else "N/A"
            description = item.select_one('p[data-component="ProductCardDescription"]').text.strip() if item.select_one('p[data-component="ProductCardDescription"]') else "N/A"
            price = item.select_one('p[data-component="Price"], p[data-component="PriceFinal"]').text.strip() if item.select_one('p[data-component="Price"], p[data-component="PriceFinal"]') else "N/A"
            discount = item.select_one('p[data-component="PriceDiscount"]').text.strip() if item.select_one('p[data-component="PriceDiscount"]') else "N/A"
            link = item.select_one("a")["href"] if item.select_one("a") else "N/A"

            products.append({"brand": brand, "description": description, "price": price, "discount": discount, "link": f"https://www.farfetch.com{link}"})

        return products
    else:
        print(f"Failed to fetch the page. Crawlbase status code: {response['headers']['pc_status']}")
        return []

# Function to scrape multiple pages
def scrape_multiple_pages(base_url, total_pages):
    all_products = []

    for page in range(1, total_pages + 1):
        paginated_url = f"{base_url}?page={page}"
        print(f"Scraping page: {page}")
        products = scrape_farfetch_listings(paginated_url)
        all_products.extend(products)

    return all_products

# Function to save data to CSV
def save_to_csv(data, filename="farfetch_listings.csv"):
    keys = data[0].keys()

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")

# Scrape Farfetch search listings
base_url = "https://www.farfetch.com/shopping/men/shoes-2/items.aspx"
all_products = scrape_multiple_pages(base_url, total_pages=5)

# Save results to CSV
if all_products:
    save_to_csv(all_products)