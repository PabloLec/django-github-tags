from django import template

register = template.Library()


@register.simple_tag
def github(*args):
    """github command takes a list of string arguments, the first part is considered
    as the endpoint path (e.g "repos" "USERNAME" "REPONAME") and the last argument
    is considered as the key to search in the response JSON (e.g "language").

    Returns:
        str: API response key value.
    """

    endpoint = args[:-1]
    key = args[-1]

    return


@register.simple_tag(name="github-raw")
def github_raw(*args):
    """github-raw command takes a list of string arguments which should be the
    endpoint path (e.g "repos" "USERNAME" "REPONAME").

    Returns:
        dict: Raw API response dict.
    """

    return
