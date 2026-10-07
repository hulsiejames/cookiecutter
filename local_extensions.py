"""Name-normalisation filters used by Cookiecutter's Jinja environment."""

import re

from cookiecutter.utils import simple_filter


@simple_filter
def pkg_name(value: str) -> str:
    """Convert a project title into an ASCII Python import name."""
    value = re.sub(r"[\s_.-]+", "_", str(value).strip().lower())
    value = re.sub(r"[^a-z0-9_]", "", value)
    return re.sub(r"_+", "_", re.sub(r"^[0-9]+", "", value))


@simple_filter
def repo_name(value: str) -> str:
    """Convert a title into a GitHub-compatible repository name."""
    value = re.sub(r"\s+", "-", str(value).strip().lower())
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9._-]", "", value))


@simple_filter
def docstring(value: str) -> str:
    """Quote a description as a Python docstring, including embedded quotes."""
    value = value.strip()
    if not value.endswith((".", "!", "?")):
        value += "."
    escaped = value.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return '"""' + escaped + '"""'
