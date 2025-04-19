import requests
from typing import Dict, Any, cast

from first_glance.core import settings


def scrape_linkedin_profile(
    linkedin_profile_url: str, mock: bool = False
) -> Dict[str, Any]:
    """Scrape information from LinkedIn profiles, Manually scrape the information from the LinkedIn profile."""

    response: str

    if mock:
        response = requests.get(
            settings.profile_data_gist_url, timeout=settings.request_time_out
        )
    else:
        params = {
            "apikey": settings.scrapein_api_key,
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            url=settings.scrapein_url, params=params, timeout=settings.request_time_out
        )

    data = cast(typ=Dict[str, Any], val=response.json().get("person"))

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url=settings.linkedin_profile_url, mock=True
        )
    )
