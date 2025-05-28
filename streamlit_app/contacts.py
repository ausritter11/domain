import os

CONTACTS_API_KEY = os.getenv("CONTACTS_API_KEY")


def search_contacts(query: str):
    """Placeholder contact search using CONTACTS_API_KEY."""
    if not CONTACTS_API_KEY:
        raise ValueError("CONTACTS_API_KEY environment variable is not set.")
    # Placeholder logic; replace with real implementation
    return [f"Contact result for {query}"]
