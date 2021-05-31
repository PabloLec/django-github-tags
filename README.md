# django-github-tags [![GitHub release (latest by date)](https://img.shields.io/github/v/release/pablolec/django-github-tags)](https://github.com/PabloLec/django-github-tags/releases/) [![GitHub](https://img.shields.io/github/license/pablolec/django-github-tags)](https://github.com/PabloLec/django-github-tags/blob/main/LICENCE)

`django-github-tags` is a Django app to access to GitHub API using tags in your Django templates.

## Installation

*The only dependency is [requests](https://pypi.org/project/requests/) which will be installed by pip during this app installation.*

```python3 -m pip install django-github-tags```

## Configuration

To integrate `django-github-tags` into your Django project, add it to your `INSTALLED_APPS` in your `settings.py` file:

``` python
INSTALLED_APPS = [
    ...,
    'django_github_tags'
]
```

:warning: Take notice of underscore/hyphens. Package name uses hyphens due to `pip` requirements, django uses underscore. :warning:

## Usage

This app is simple and goes straight to the point. It lets you use Django template tags as GitHub API queries.

To use it in your template `.html` file, add:

``` html
{% load django_github_tags %}
```

There are two possible tags: `github` and `github-raw`.

### `github`

**This tag requires an endpoint path and a key to search into the API response. The output will be a string.**

Typical usage is:

``` html
{% github "API_ENDPOINT" "PATH_ARG1" "PATH_ARG2" "PATH_ARGX" "KEY" %}
```

For example, to access [recoverpy](https://github.com/PabloLec/recoverpy) repository programming language, you can use:

``` html
Monty {% github "repos" "pablolec" "recoverpy" "language" %}
```

And Django will generate:
```
Monty Python
```

### `github-raw`

**This tag requires only an endpoint path. The output will be a dictionary.**

Typical usage is:
``` html
{% github "API_ENDPOINT" "PATH_ARG1" "PATH_ARG2" "PATH_ARGX" %}
```

For example, to manipulate my own GitHub profile, I can use:

``` html
{% github-raw "users" "pablolec" as myprofile %}

Check out my cool profile at: {% myprofile.html_url %}

And by the way, I live in {% myprofile.location %}.
```

And Django will generate:

```
Check out my cool profile at: https://github.com/PabloLec
And by the way, I live in France.
```

## General Principle

Anything you can do with GET requests and GitHub REST API, you can also do it with `django-github-tags`. And that's a lot.

**To have a full tour of the API capabilities, refer to the [official documentation](https://docs.github.com/en/rest).**

Keep in mind that if you want to get a simple string result for one particular key, use the `github` command.
If you want the full API response to use it as a dictionary, use `github-raw` command.


## Examples

There is of course an infinity of potential usage. Let it be:
- Provide users dynamic GitHub profile data.
- Display a repo stars, fork count, etc.
- Track latest issue.
- Add to a user profile its assigned issues or send notifications.
- Get newest PR commits, comments.
- Sync users profile pic with GitHub's pic.
- List latest `good first issue` labels.
- A GitHub [insert your filter] search engine

Well, the only limit is your imagination (and [documentation](https://docs.github.com/en/rest)).

## License


django-github-tags is released under the [GPL-3.0 License](https://github.com/PabloLec/django-github-tags/blob/main/LICENCE). 
