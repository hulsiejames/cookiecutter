"""Resolve editable-install versions; builds replace the call with a fixed version."""


def _get_version() -> str:
    from pathlib import Path

    from versioningit import get_version

    root = Path(__file__).resolve().parents[{{ cookiecutter.package_name.split('.')|length + 1 }}]
    return get_version(project_dir=root)


__version__ = _get_version()
