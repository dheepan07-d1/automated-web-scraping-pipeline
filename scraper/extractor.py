
from bs4 import BeautifulSoup


def extract_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = []

    # Find all book containers
    book_cards = soup.select("article.product_pod")

    for book in book_cards:
        # Extract title
        title_tag = book.select_one("h3 a")
        title = title_tag.get("title", "").strip() if title_tag else "Unknown"

        # Extract price
        price_tag = book.select_one(".price_color")
        price = price_tag.text.strip() if price_tag else "£0.00"

        # Extract availability
        availability_tag = book.select_one(".availability")
        availability = (
            availability_tag.get_text(strip=True)
            if availability_tag else "Unknown"
        )

        # Extract rating
        rating_tag = book.select_one(".star-rating")
        rating = "Unknown"

        if rating_tag:
            rating_classes = rating_tag.get("class", [])
            for value in ["One", "Two", "Three", "Four", "Five"]:
                if value in rating_classes:
                    rating = value
                    break

        books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    return books
