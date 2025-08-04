# This is used to install our local packages present in src to our environment , since when running anything
# inside src, we might get an issue even after requirements.txt, therefore to install src also in our environment
# we use setup.py file and pyproject.toml

from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Subrat Bahuguna",
    author_email="bahuguna.subrat211996@gmail.com",
    packages=find_packages()
)