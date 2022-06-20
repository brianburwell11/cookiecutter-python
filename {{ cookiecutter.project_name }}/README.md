# {{ cookiecutter.project_name }}

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/) 
[![Github release](https://img.shields.io/badge/release-{{ cookiecutter.version }}-blue.svg?style=flat-square)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/releases/tag/{{ cookiecutter.version }}){% if cookiecutter.atlassian_project %}
[![Confluence](https://img.shields.io/badge/-Confluence-fbf7f5.svg?logo=confluence&labelColor=dfe1e5&logoColor=0052cc&style=flat-square)](https://{{ cookiecutter.atlassian_project }}.atlassian.net/wiki/home/recent){% endif %}{% if cookiecutter.documentation != "None" %}
[![Documentation](https://img.shields.io/badge/-Documentation-2980b9.svg?logo=readthedocs&labelColor=2980b9&logoColor=FFFFFF&style=flat-square)][documentation]{% endif %}

{{ cookiecutter.project_short_description }}

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
{% if cookiecutter.documentation == "GitHub Wiki" %}
[documentation]: https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/wiki
{% elif cookiecutter.documentation == "GitHub Pages" %}
[documentation]: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_name }}/
{% endif %}