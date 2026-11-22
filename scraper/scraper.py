
import requests
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def create_session():
    session = requests.Session()

    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; BookDataResearchBot/1.0)"
    })

    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)

    return session


def fetch_page(session, page_number):
    url = BASE_URL.format(page_number)

    try:
        response = session.get(url, timeout=15)
        response.raise_for_status()
        print(f"Successfully fetched page {page_number}")
        return response.text

    except requests.RequestException as error:
        print(f"Error fetching page {page_number}: {error}")
        return None


def scrape_pages(max_pages=5):
    session = create_session()
    pages = []

    for page_number in range(1, max_pages + 1):
        html = fetch_page(session, page_number)

        if html is None:
            break

        pages.append(html)
        time.sleep(1)  # Polite delay between requests

    session.close()
    return pages
