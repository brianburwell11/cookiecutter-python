# REPO-NAME

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat-square)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Github release](https://img.shields.io/badge/release-0.1.0-blue.svg?style=flat-square)](https://github.com/brianburwell11/REPO-NAME/releases/tag/0.1.0)
<!-- [![Confluence](https://img.shields.io/badge/-Confluence-fbf7f5.svg?logo=confluence&labelColor=dfe1e5&logoColor=0052cc&style=flat-square)](https://my-project.atlassian.net/wiki/home/recent) -->


## Getting Started

### Modifying this Template Repository

This repository is a template that can be used to start new python projects. It comes with boilerplate configuration that enforces good coding practices like consistent code formatting ([black](https://black.readthedocs.io/en/stable/)), dependency management ([poetry](https://python-poetry.org/docs/)), commit messages and project versioning/releases ([commitizen](https://commitizen-tools.github.io/commitizen/)).

To set up this template, replace all instances of `PACKAGE_NAME` with the name of your python package and all instances of `REPO-NAME` with the name of the repository on Github. **Don't forget to also change the name of the directory `PACKAGE_NAME/`.**

To enable [automated documentation deployment to GitHub Pages](https://pdoc.dev/docs/pdoc.html), enable GitHub Pages in your repository settings[^1].
> Settings > Pages > Source > `master` > `/(root)`

[^1]: GitHub Pages is only available (for free) for public repositories

To enable [automated releases via commitizen](https://commitizen-tools.github.io/commitizen/tutorials/github_actions/), add a personal access token as a secret to your copied repository.
> 1. Create a personal access token. [Follow the instructions here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-token). And copy the generated key
> 2. Create a secret called PERSONAL_ACCESS_TOKEN, with the copied key, by going to your project repository and then Settings > Secrets > Add new secret.

Finally, delete this section of the README.

### Installing Dependencies

This project uses [Poetry][poetry] for dependency management.

```sh
poetry install
poetry run pre-commit install
```

## Installation

`PACKAGE_NAME` can be installed directly from the GitHub repository using one of these commands:

```sh
pip install git+ssh://git@github.com/brianburwell11/REPO-NAME.git@master
```

```sh
poetry add git+ssh://git@github.com/brianburwell11/REPO-NAME.git#master
```

## Usage

<!-- add simple usage instructions here  -->



<!-- links -->
[poetry]: https://python-poetry.org/docs/

[changelog]: docs/CHANGELOG.md
