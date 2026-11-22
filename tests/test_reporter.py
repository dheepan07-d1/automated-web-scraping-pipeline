
import pandas as pd
from scraper.reporter import generate_report


def test_generate_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "output").mkdir()

    dataframe = pd.DataFrame({
        "title": ["Book A", "Book B"],
        "price": [20.0, 40.0],
        "rating": [4, 5],
        "availability": ["In stock", "In stock"]
    })

    generate_report(dataframe)

    report_file = tmp_path / "output" / "summary_report.txt"

    assert report_file.exists()

    content = report_file.read_text(encoding="utf-8")

    assert "Total Books Scraped : 2" in content
    assert "Average Book Price" in content


def test_empty_report():
    dataframe = pd.DataFrame(
        columns=["title", "price", "rating", "availability"]
    )

    assert generate_report(dataframe) is None
