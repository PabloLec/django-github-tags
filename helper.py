import requests
import json

import django_github_tags.errors as _ERRORS


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

    if type(response) == dict and response.get("message") == "Not Found":
        raise _ERRORS.GitHubBadEndpoint(url=url)

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

    try:
        value = response[key.lower()]
    except KeyError:
        raise _ERRORS.GitHubBadKey(current_key=key, existing_keys=tuple(response.keys()))
    except TypeError:
        raise _ERRORS.GitHubBadFormat(current_type=type(response))

    return value
