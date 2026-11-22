
# Automated Web Scraping & Data Extraction Pipeline

## Overview
A Python-based web scraping pipeline that extracts book information from Books to Scrape, cleans the data, exports structured files, and generates an analytical report.

## Features
- Web scraping using Requests and BeautifulSoup
- Extracts book titles, prices, ratings, and availability
- Handles HTTP errors and retries
- Polite request delays
- Data cleaning using Pandas
- CSV and JSON exports
- Automated analytical report
- Unit testing with Pytest

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Pytest
- Pytest-Cov

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
│   ├── test_scraper.py
│   ├── test_transformer.py
│   └── test_reporter.py
├── output/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/dheepan07-d1/automated-web-scraping-pipeline.git
cd automated-web-scraping-pipeline
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

The pipeline fetches five pages by default.

## Output Files

The output directory contains:

- books_data.csv
- books_data.json
- summary_report.txt

## Run Tests

```bash
python -m pytest -v
```

Run tests with coverage:

```bash
python -m pytest --cov=scraper --cov-report=term-missing
```

## Test Results

- 11 automated tests passed
- 99% overall code coverage

## Data Source

https://books.toscrape.com/

This is a public demo website intended for web scraping practice.

## Author

Dheepan Pgit status
