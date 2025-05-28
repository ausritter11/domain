import os

LINKEDIN_API_KEY = os.getenv("LINKEDIN_API_KEY")


def lookup_profile(name: str):
    """Placeholder LinkedIn profile lookup using LINKEDIN_API_KEY."""
    if not LINKEDIN_API_KEY:
        raise ValueError("LINKEDIN_API_KEY environment variable is not set.")
    # Placeholder logic; replace with real implementation
    return f"LinkedIn profile info for {name}"
