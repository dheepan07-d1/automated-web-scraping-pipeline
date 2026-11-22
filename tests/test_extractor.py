
from scraper.extractor import extract_books


def test_extract_books():
    html = """
    <article class="product_pod">
        <p class="star-rating Three"></p>
        <h3>
            <a title="Test Book" href="#">Test Book</a>
        </h3>
        <p class="price_color">£25.99</p>
        <p class="availability">In stock</p>
    </article>
    """

    books = extract_books(html)

    assert len(books) == 1
    assert books[0]["title"] == "Test Book"
    assert books[0]["price"] == "£25.99"
    assert books[0]["rating"] == "Three"
    assert "In stock" in books[0]["availability"]


def test_empty_html():
    books = extract_books("<html><body></body></html>")

    assert books == []
