class GitHubBadEndpoint(Exception):
    """Exception raised when GitHub API does not find requested endpoint."""

    def __init__(self, url: str):
        self.message = f"Empty response from Github API with request: {url}. Verify given arguments."
        super().__init__(self.message)


class GitHubBadKey(Exception):
    """Exception raised when requested key is not find within API response."""

    def __init__(self, current_key: str, existing_keys: tuple):
        self.message = f"Key '{current_key}' cannot be found. Existing keys are: {existing_keys}."
        super().__init__(self.message)


class GitHubBadFormat(Exception):
    """Exception raised when received data format is not adapted for 'github' tag."""

    def __init__(self, current_type: type):
        self.message = (
            f"Current response type is '{current_type}'. 'github' "
            "tag cannot handle this type of data. To get raw response use 'github-raw' tag."
        )
        super().__init__(self.message)
