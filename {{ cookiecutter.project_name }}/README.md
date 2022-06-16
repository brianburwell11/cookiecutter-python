# {{ cookiecutter.project_name }}

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Github release](https://img.shields.io/badge/release-{{ cookiecutter.version }}-blue.svg?style=flat-square)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/releases/tag/{{ cookiecutter.version }}){% if cookiecutter.atlassian_project %}
[![Confluence](https://img.shields.io/badge/-Confluence-fbf7f5.svg?logo=confluence&labelColor=dfe1e5&logoColor=0052cc&style=flat-square)](https://{{ cookiecutter.atlassian_project }}.atlassian.net/wiki/home/recent){% endif %}

## Getting Started

### Installing Dependencies

This project uses [Poetry][poetry] for dependency management.

```sh
poetry install
poetry run pre-commit install
```

## Installation

**{{ cookiecutter.project_slug }}** can be installed directly from the GitHub repository using one of these commands:

```sh
pip install git+ssh://git@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git@master
```

```sh
poetry add git+ssh://git@github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git#master
```

## Usage

<!-- add simple usage instructions here  -->



<!-- links -->
[poetry]: https://python-poetry.org/docs/

[changelog]: docs/CHANGELOG.md
