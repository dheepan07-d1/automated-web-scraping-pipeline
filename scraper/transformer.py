
import pandas as pd


def transform_books(books):
    cleaned_books = []

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    for book in books:
        # Clean and convert price
        price_text = (
            book["price"]
            .replace("Â", "")
            .replace("£", "")
            .strip()
        )
        price = float(price_text)

        # Convert rating into numeric value
        rating = rating_map.get(book["rating"], None)

        cleaned_books.append({
            "title": book["title"].strip(),
            "price": price,
            "rating": rating,
            "availability": book["availability"].strip()
        })

    return pd.DataFrame(cleaned_books)


def save_data(dataframe):
    dataframe.to_csv("output/books_data.csv", index=False)

    dataframe.to_json(
        "output/books_data.json",
        orient="records",
        indent=4,
        force_ascii=False
    )

    print("CSV and JSON files saved successfully!")
