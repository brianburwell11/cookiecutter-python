import os
import shutil
import subprocess

import yaml


MANIFEST = "manifest.yaml"


def delete_resources_for_disabled_features():
    with open(MANIFEST, "r") as manifest_file:
        manifest = yaml.safe_load(manifest_file)
        for feature in manifest["features"]:
            if not feature["enabled"]:
                for resource in feature["resources"]:
                    delete_resource(resource)
    delete_resource(MANIFEST)


def delete_resource(resource):
    if os.path.isfile(resource):
        os.remove(resource)
    elif os.path.isdir(resource):
        shutil.rmtree(resource)


if __name__ == "__main__":
    delete_resources_for_disabled_features()
    subprocess.run(["git", "init"])
    try:
        # install poetry dependencies
        subprocess.run(["poetry", "install"], check=True)
    except subprocess.CalledProcessError:
        print(
            "It looks like poetry isn't installed on this machine.",
            "Please install poetry by following the instructions at https://python-poetry.org/docs/#installation",
            "and then run the following commands from within the generated project directory:",
            "\n\tpoetry install",
            "\n\tpre-commit install",
            "\n",
        )
    else:
        subprocess.run(["poetry", "run", "pre-commit", "install"])
    finally:
        print(
            "\nBefore making your first push, don't forget to add a Personal Access Token to your repository",
            end=" ",
        )
        if {{cookiecutter.documentation == "GitHub Wiki"}}:
            print("and create a blank page in your repository's wiki")
