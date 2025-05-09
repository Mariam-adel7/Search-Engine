# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else ""

        text = soup.get_text(separator=' ', strip=True)

        return {
            "url": url,
            "title": title,
            "content": text
        }

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None
