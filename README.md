# Cookiecutter

A reusable template for Python package repositories, with automated versioning,
tests, linting, type checking, documentation and GitHub workflows.

## Usage

Install [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) with
[pipx](https://pipx.pypa.io/stable/), then generate a package:

```sh
pipx install cookiecutter
cookiecutter gh:hulsiejames/cookiecutter
```

If you already installed Cookiecutter through pipx, run `pipx upgrade cookiecutter`.
Use Cookiecutter 2.4 or newer. Git is required to fetch the template from GitHub.
The template itself does not need to be installed as a Python package.

The command asks nine questions and creates a repository folder in your current
directory. To choose another location, add `--output-dir path/to/projects`.
Use `--no-input` to accept defaults, or supply answers as `key=value` arguments:

```sh
cookiecutter gh:hulsiejames/cookiecutter --no-input project_name="My Package"
```

## Questions

| Question | Default and purpose |
| --- | --- |
| Human-Readable Project Name | `Package Name`; the title in READMEs and documentation. |
| Full Package Name | Derived from the title, for example `my_package`; used for Python imports and distribution metadata. |
| Full Repository Name | Derived from the title, for example `my-package`; names the generated folder and GitHub repository. |
| Author | `James Hulse`; change this for the person or organisation responsible for the package. |
| GitHub User or Organisation Account | `hulsiejames`; change this to the account owning your repository. |
| GitHub Source Code URL | Derived from the account and repository name; used for source links and Git's origin. |
| Brief package description | `Package description`; included in metadata, the README and documentation. |
| Initialise local git repository? | `false`; `true` creates `main`, commits the scaffold and adds origin. |
| Push repository to GitHub? | `false`; `true` pushes `main` to an existing empty repository. Requires Git initialisation. |

Names are normalised into lowercase ASCII defaults. Spaces become underscores in
import names and hyphens in repository names. You can override either value.
For a namespace package, enter a dotted import name such as `acme.tools`; the
template creates its source folders and version-file paths accordingly.

## GitHub setup

To enable automatic push, first [create an empty repository](https://github.com/new)
with the intended owner, name and visibility. Leave README, .gitignore and licence
initialisation disabled. Then check the source URL in the template and answer
`yes` to both Git questions. Configure your Git name, email and authentication
before generating with Git enabled.

You can also generate with both Git options disabled, then initialise and publish
the folder with GitHub Desktop or the Git command line.

## Template Details

### Package structure

The scaffold uses a `src/` layout and Python 3.11 or newer. Package code lives
under `src/`, tests under `tests/`, documentation under `docs/`, and runnable
or display-only documentation examples under `examples/`.

`pyproject.toml` defines build metadata, tool settings and development extras.
Runtime dependencies come from `requirements.txt`, development tools from
`requirements_dev.txt`, and documentation tools from `docs/requirements.txt`.
A `py.typed` marker declares support for type hints.

### Development

After generation, initialise Git if you did not enable it in the prompts, then
install the package and its development tools from the generated folder:

```sh
python -m pip install -e ".[dev,docs]"
ruff format .
ruff check .
pylint src
mypy src
pytest
```

Ruff handles formatting and a broad set of lint checks; Pylint supplies additional
checks and MyPy checks types. Pytest runs tests and doctests with parallel workers,
coverage for the selected package, an XML coverage report and JUnit test results.
Replace the sample test with tests for your package.

The scaffold ignores local environments, tool output, notebooks and common data,
database, document and archive files. Add explicit exceptions to `.gitignore`
when a fixture or example data file belongs in version control.

### Versions and builds

[Versioningit](https://versioningit.readthedocs.io/en/stable/) derives versions
from Git tags. Release tags use the form `v0.1.0`; before your first release the
base version is `0.0.1`. Additional commits and uncommitted changes appear in
development versions. Editable installs read the current version from Git;
distributions contain a static version so installations do not need Git.

Build a wheel and source distribution with:

```sh
python -m pip install build
python -m build
```

### Documentation

Sphinx provides a quick-start guide, user guide, tutorial, API reference and example
gallery using the PyData theme. NumPy-style docstrings populate API pages, source
links lead to GitHub, and class templates allow inherited members to be selected.
The theme includes links to issues and releases, a documentation edit button,
and a project title in place of a logo. `SPHINX_INCLUDE_TODOS=false` hides TODOs.

Build HTML documentation from the generated folder:

```sh
sphinx-build -b html docs/source docs/build/html
```

The `docs/Makefile` and Windows `docs/make.bat` also support `make html` from
`docs/`. Scripts named `run_*.py` execute during gallery builds; other example
scripts are displayed without execution.

### Automation and publishing

Generated GitHub Actions check formatting, linting, typing, tests and package
builds on pushes and pull requests to `main`. Draft pull requests wait until they
are ready for review. Build and test matrices cover Python 3.11–3.14; tests run
on Linux and Windows. Codecov uploads use a `CODECOV_TOKEN` repository secret.
Monthly Dependabot checks propose major Python dependency updates and GitHub
Action updates, with limits on the number of open pull requests.

The PyPI release workflow is disabled initially. Configure a GitHub environment
named `release` and a [PyPI trusted publisher](https://docs.pypi.org/trusted-publishers/)
using the repository and `release.yml`, then remove `if: false` from that workflow.
Publishing a GitHub release will then build and publish the distribution.

To publish documentation, import the generated repository into
[Read the Docs](https://app.readthedocs.org/dashboard/import/). The included
`.readthedocs.yaml` installs the package and builds its Sphinx documentation.
Update the generated documentation URLs if you choose a different project slug.

### Licences

This template's original implementation is MIT licensed. Generated packages
start with the GNU GPLv3 text in their own `LICENSE`. Review that choice before
publishing your package and update its licence and metadata if appropriate.

### Editing the template

`cookiecutter.json` defines the questions, hidden derived values and rendering
options. `local_extensions.py` supplies name-normalisation filters. The hooks
embed this guide in the default package README and implement optional Git setup.
The directory named for `cookiecutter.project_slug` contains generated files.
Sphinx's Jinja templates and selected workflow files are copied without rendering.
