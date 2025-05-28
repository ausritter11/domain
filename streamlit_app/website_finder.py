import os

WEBSITE_FINDER_API_KEY = os.getenv("WEBSITE_FINDER_API_KEY")


def find_website(company: str):
    """Placeholder website finder using WEBSITE_FINDER_API_KEY."""
    if not WEBSITE_FINDER_API_KEY:
        raise ValueError("WEBSITE_FINDER_API_KEY environment variable is not set.")
    # Placeholder logic; replace with real implementation
    return f"https://{company}.com"
