# {{ cookiecutter.__readable_name }}

[![Python versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }})](https://pypi.org/project/{{ cookiecutter.package_name }}/)
[![Release](https://img.shields.io/github/v/release/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }})]({{ cookiecutter.github_url }}/releases)
[![Conda](https://img.shields.io/conda/v/conda-forge/{{ cookiecutter.package_name }})](https://anaconda.org/conda-forge/{{ cookiecutter.package_name }})
[![Tests](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }}/tests.yml?label=tests)]({{ cookiecutter.github_url }}/actions)
[![Coverage](https://img.shields.io/codecov/c/github/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }})](https://app.codecov.io/gh/{{ cookiecutter.github_org }}/{{ cookiecutter.project_slug }})
[![Documentation](https://img.shields.io/readthedocs/{{ cookiecutter.__docs_name }})]({{ cookiecutter.__readthedocs_url }}/stable/)

{{ cookiecutter.description }}

> This package is under development. Check the release notes before upgrading.

## Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Contact](#contact)
{% if cookiecutter.package_name == "package_name" %}
- [Template Usage](#template-usage)
{% endif %}

## Overview

Describe the problem this package solves, who uses it and its main features here.
List planned features separately from features already available in a release.

## Installation

Once published to PyPI:

```sh
pip install {{ cookiecutter.package_name }}
```

If you also publish a conda-forge package:

```sh
conda install -c conda-forge {{ cookiecutter.package_name }}
```

Before publishing, install directly from GitHub:

```sh
pip install "git+{{ cookiecutter.github_url }}"
```

Append `@v0.1.0` or a branch name to the Git URL to select a particular revision.
See [requirements.txt](requirements.txt) for runtime dependencies.

## Usage

```python
import {{ cookiecutter.package_name }}
```

Add a short working example here. If your package exposes a command line or GUI,
describe how to launch it and link to its guide.

## Documentation

The [documentation]({{ cookiecutter.__readthedocs_url }}/stable/) includes
a quick-start guide, tutorials, examples and an API reference.

## Contributing

Open an [issue]({{ cookiecutter.github_url }}/issues) to discuss bugs or ideas,
or submit a pull request. Install development dependencies with
`python -m pip install -e ".[dev,docs]"` and run `ruff check .`, `ruff format --check .`,
`pylint src`, `mypy src` and `pytest` before submitting changes.
See [LICENSE](LICENSE) for this package's licence.

## Contact

Maintained by {{ cookiecutter.author }}. Use the
[issue tracker]({{ cookiecutter.github_url }}/issues) for package questions.

{% if cookiecutter.package_name == "package_name" %}
## Template Usage

Choose your package and repository names when running Cookiecutter, then replace
the placeholder introduction, usage example and sample test with your own content.
Remove this section when the package README is ready.

{{ cookiecutter._template_details }}
{% endif %}
