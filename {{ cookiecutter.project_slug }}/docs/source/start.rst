Quick start
===========

Installation
------------

After the package is published, install it with pip:

.. code-block:: sh

   pip install {{ cookiecutter.package_name }}

For a development checkout, clone the repository and install the development extras:

.. code-block:: sh

   git clone {{ cookiecutter.github_url }}
   cd {{ cookiecutter.project_slug }}
   python -m pip install -e ".[dev,docs]"

First use
---------

.. code-block:: python

   import {{ cookiecutter.package_name }}

Add a short example of the package's public API to this page.
