import requests
import json


def fetch(endpoint: tuple):
    """Uses requests to fetch API response for current endpoint.

    Args:
        endpoint (tuple): List of strings composing API endpoint path.

    Raises:
        _ERRORS.GitHubBadEndpoint: If the API returns a "Not Found" error.

    Returns:
        dict: Raw API response dict.
    """

    url = f"https://api.github.com/{'/'.join(endpoint)}"
    response = json.loads(requests.get(url).text)

    return response


def get_value(response: dict, key: str):
    """Get requested key value in API response dict.

    Args:
        response (dict): Raw API response dict.
        key (str): Requested key.

    Raises:
        _ERRORS.GitHubBadKey: If the requested key is not found within current
            API response dict.
        _ERRORS.GitHubBadFormat: If the API response format is not a dict when
            used with 'github' command.

    Returns:
        str: Requested key value.
    """

    value = response[key.lower()]

    return value
