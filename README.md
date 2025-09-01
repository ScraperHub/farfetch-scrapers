<a href="https://crawlbase.com/signup?utm_source=github&utm_medium=readme&utm_campaign=crawling_api_banner" target="_blank">
  <img src="https://github.com/user-attachments/assets/afa4f6e7-25fb-442c-af2f-b4ddcfd62ab2" 
       alt="crawling-api-cta" 
       style="max-width: 100%; border: 0;">
</a>


# farfetch-scrapers

## Description

This repository contains Python-based scrapers for extracting product data from [Farfetch](https://www.farfetch.com/). These scrapers use the [Crawlbase Crawling API](https://crawlbase.com/crawling-api-avoid-captchas-blocks) to bypass JavaScript rendering, CAPTCHA challenges, and anti-bot protections, enabling smooth data extraction.

➡ Read the full blog [here](https://crawlbase.com/blog/how-to-scrape-retail-data-from-farfetch/) to learn more.

## Scrapers Overview

### Farfetch Search Results Scraper

The Farfetch Search Results Scraper (`farfetch_serp_scraper.py`) extracts product details from search listings, including:

- **Brand Name**
- **Product Description**
- **Price**
- **Discount (if available)**
- **Product URL**

It supports pagination, allowing multiple search results pages to be scraped. The extracted data is saved in a CSV file.

### Farfetch Product Page Scraper

The Farfetch Product Page Scraper (`farfetch_product_page_scraper.py`) extracts product details from individual product pages, including:

- **Product Blurb**
- **Brand Name**
- **Price**
- **Full Product Description**

This scraper takes product URLs from the search listings scraper and extracts product details, saving the data in a CSV file.

## Environment Setup

Ensure that Python is installed on your system. Check the version using:

```bash
# Use python3 if you're on Linux/macOS
python --version
```

Install the required dependencies:

```bash
pip install crawlbase beautifulsoup4
```

- **Crawlbase** – Handles JavaScript rendering and bypasses bot protections.
- **BeautifulSoup** – Parses and extracts structured data from HTML.

## Running the Scrapers

### 1. Get Your Crawlbase Access Token

- Sign up for Crawlbase [here](https://crawlbase.com/signup) to get an API token.
- Use the **JS token** for Farfetch scraping, as the site relies on JavaScript-rendered content.

### 2. Run the Search Listings Scraper

This scraper extracts product listings and saves them in `farfetch_listings.csv`:

```bash
# Use python3 if required (for Linux/macOS)
python farfetch_serp_scraper.py
```

### 3. Run the Product Page Scraper

Once you have the search results, extract detailed product information using:

```bash
python farfetch_product_page_scraper.py
```

This will fetch and save product details in `farfetch_product_details.csv`.

## To-Do List

- Add more product details (e.g., sizes, materials, colors).
- Support JSON output in addition to CSV.
- Improve pagination to handle dynamic page numbers.
- Add better error handling and retries for failed requests.

## Features

- **Bypasses anti-bot protections** using Crawlbase.
- **Handles JavaScript-rendered content** efficiently.
- **Extracts structured product data** in CSV format for easy analysis.
- **Supports pagination** to scrape multiple search result pages.
