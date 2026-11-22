# Automated Web Scraping & Data Extraction Pipeline

## Project Overview
This project is an automated web scraping and data extraction pipeline developed using Python. It extracts book information from Books to Scrape, processes the collected data, and generates structured CSV and JSON files along with an analytical report.

## Objectives
- Automate website data extraction.
- Extract book titles, prices, ratings and availability.
- Clean and transform raw data.
- Export structured datasets.
- Generate analytical summaries.
- Implement automated testing.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Pytest
- HTML Parsing

## Project Structure
```text
automated-web-scraping-pipeline/
├── scraper/
│   ├── __init__.py
│   ├── scraper.py
│   ├── extractor.py
│   ├── transformer.py
│   └── reporter.py
├── tests/
│   ├── test_extractor.py
│   └── test_transformer.py
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Features
1. Automated web scraping using Requests.
2. Retry handling for temporary request failures.
3. HTML parsing using BeautifulSoup.
4. Extraction of book details.
5. Data cleaning and transformation using Pandas.
6. CSV and JSON data export.
7. Automated analytical report generation.
8. Unit testing using Pytest.

## Extracted Data
- Book Title
- Price
- Rating
- Availability

## Execution Results
- Pages scraped: 5
- Total books extracted: 100
- Average price: £34.56
- Minimum price: £10.16
- Maximum price: £58.11
- Average rating: 2.93 / 5

## Generated Files
- `books_data.csv`
- `books_data.json`
- `summary_report.txt`

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd automated-web-scraping-pipeline

python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Run Tests

```bash
python -m pytest -v
```

## Test Results
All 4 automated tests passed successfully.

## Data Source
[Books to Scrape](https://books.toscrape.com/)

This is a demonstration website intended for web scraping practice.

## Author
Developed as part of a Python Software Developer Internship Task.