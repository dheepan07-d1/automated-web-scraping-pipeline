
from unittest.mock import Mock
import requests

from scraper import scraper


def test_create_session():
    session = scraper.create_session()

    assert "User-Agent" in session.headers
    assert "BookDataResearchBot" in session.headers["User-Agent"]

    session.close()


def test_fetch_page_success(monkeypatch):
    mock_response = Mock()
    mock_response.text = "<html>Test</html>"
    mock_response.raise_for_status.return_value = None

    mock_session = Mock()
    mock_session.get.return_value = mock_response

    result = scraper.fetch_page(mock_session, 1)

    assert result == "<html>Test</html>"
    mock_session.get.assert_called_once()


def test_fetch_page_failure(monkeypatch):
    mock_session = Mock()
    mock_session.get.side_effect = requests.RequestException("Network error")

    result = scraper.fetch_page(mock_session, 1)

    assert result is None


def test_scrape_pages(monkeypatch):
    monkeypatch.setattr(
        scraper, "create_session", lambda: Mock(close=Mock())
    )

    monkeypatch.setattr(
        scraper, "fetch_page",
        lambda session, page: f"HTML page {page}"
    )

    monkeypatch.setattr(scraper.time, "sleep", lambda seconds: None)

    pages = scraper.scrape_pages(max_pages=3)

    assert len(pages) == 3
    assert pages[0] == "HTML page 1"
