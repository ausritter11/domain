from typing import List, Dict, Any


def get_top_contacts(email_client: Any, n: int = 5) -> List[str]:
    """Return the top N contacts based on message count."""
    stats: Dict[str, int] = email_client.get_contacts_stats()
    return [contact for contact, _ in sorted(stats.items(), key=lambda x: x[1], reverse=True)[:n]]


def get_first_google_result(query: str, search_api: Any) -> str:
    """Return the first result link for a Google query."""
    results = search_api.search(query)
    return results[0]["link"] if results else ""


def find_linkedin_profile(name: str, search_api: Any) -> str:
    """Find the first LinkedIn profile for a given name."""
    query = f"{name} linkedin"
    return get_first_google_result(query, search_api)
