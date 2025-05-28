import pytest
from unittest.mock import MagicMock

from contacts import get_top_contacts, get_first_google_result, find_linkedin_profile


def test_get_top_contacts():
    client = MagicMock()
    client.get_contacts_stats.return_value = {
        "alice@example.com": 10,
        "bob@example.com": 5,
        "carol@example.com": 1,
    }
    top = get_top_contacts(client, n=2)
    assert top == ["alice@example.com", "bob@example.com"]
    client.get_contacts_stats.assert_called_once()


def test_get_first_google_result():
    api = MagicMock()
    api.search.return_value = [
        {"link": "http://example.com/result1"},
        {"link": "http://example.com/result2"},
    ]
    link = get_first_google_result("test query", api)
    assert link == "http://example.com/result1"
    api.search.assert_called_once_with("test query")


def test_find_linkedin_profile():
    api = MagicMock()
    api.search.return_value = [
        {"link": "http://linkedin.com/in/johndoe"}
    ]
    link = find_linkedin_profile("John Doe", api)
    assert link == "http://linkedin.com/in/johndoe"
    api.search.assert_called_once_with("John Doe linkedin")
