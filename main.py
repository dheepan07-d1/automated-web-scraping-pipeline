
import os

from scraper.scraper import scrape_pages
from scraper.extractor import extract_books
from scraper.transformer import transform_books, save_data
from scraper.reporter import generate_report


def main():
    print("\nStarting Web Scraping Pipeline...\n")

    # Create output folder if it doesn't exist
    os.makedirs("output", exist_ok=True)

    # Step 1: Fetch website pages
    pages = scrape_pages(max_pages=5)

    # Step 2: Extract book details
    all_books = []

    for page in pages:
        books = extract_books(page)
        all_books.extend(books)

    print(f"\nTotal books extracted: {len(all_books)}")

    if not all_books:
        print("No books found. Please check the website connection.")
        return

    # Step 3: Transform the data
    dataframe = transform_books(all_books)

    # Step 4: Save CSV and JSON
    save_data(dataframe)

    # Step 5: Generate analytical report
    generate_report(dataframe)

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    main()
