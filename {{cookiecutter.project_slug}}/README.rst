{{cookiecutter.project_slug}}
{{'=' * cookiecutter.project_slug|length}}

.. image:: https://travis-ci.org/aioworkers/{{cookiecutter.project_slug}}.svg?branch=master
  :target: https://travis-ci.org/aioworkers/{{cookiecutter.project_slug}}

.. image:: https://img.shields.io/pypi/pyversions/{{cookiecutter.project_slug}}.svg
  :target: https://pypi.python.org/pypi/{{cookiecutter.project_slug}}
  :alt: Python versions

.. image:: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg
  :target: https://pypi.python.org/pypi/{{cookiecutter.project_slug}}


Development
-----------

Install dev requirements:


.. code-block:: shell

    pipenv install --dev --skip-lock


Run tests:

.. code-block:: shell

    pytest