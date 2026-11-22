
from scraper.transformer import transform_books


def test_transform_books():
    books = [
        {
            "title": "Test Book",
            "price": "£25.99",
            "rating": "Three",
            "availability": "In stock"
        },
        {
            "title": "Second Book",
            "price": "£15.50",
            "rating": "Five",
            "availability": "In stock"
        }
    ]

    df = transform_books(books)

    assert len(df) == 2
    assert df.iloc[0]["price"] == 25.99
    assert df.iloc[0]["rating"] == 3
    assert df.iloc[1]["rating"] == 5


def test_empty_transform():
    df = transform_books([])

    assert df.empty

def test_save_data(tmp_path, monkeypatch):
    from scraper.transformer import save_data
    import pandas as pd

    monkeypatch.chdir(tmp_path)
    (tmp_path / "output").mkdir()

    dataframe = pd.DataFrame({
        "title": ["Test Book"],
        "price": [25.99],
        "rating": [4],
        "availability": ["In stock"]
    })

    save_data(dataframe)

    assert (tmp_path / "output" / "books_data.csv").exists()
    assert (tmp_path / "output" / "books_data.json").exists()


