{{cookiecutter.project_slug}}
{{'=' * cookiecutter.project_slug|length}}

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg
  :target: https://pypi.org/project/{{cookiecutter.project_slug}}

.. image:: https://github.com/aioworkers/{{cookiecutter.project_slug}}/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/{{cookiecutter.project_slug}}/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/{{cookiecutter.project_slug}}

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json
  :target: https://github.com/charliermarsh/ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  :alt: Code style: black

.. image:: https://img.shields.io/badge/types-Mypy-blue.svg
  :target: https://github.com/python/mypy

.. image:: https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest
  :target: https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}.svg
  :target: https://pypi.org/project/{{cookiecutter.project_slug}}

.. image:: https://img.shields.io/pypi/dm/{{cookiecutter.project_slug}}.svg
  :target: https://pypi.org/project/{{cookiecutter.project_slug}}

.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
  :alt: Hatch project
  :target: https://github.com/pypa/hatch


Development
-----------

Check code:

.. code-block:: shell

    hatch run lint:all


Format code:

.. code-block:: shell

    hatch run lint:fmt


Run tests:

.. code-block:: shell

    hatch run pytest


Run tests with coverage:

.. code-block:: shell

    hatch run cov
