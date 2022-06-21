from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt

    return This function is going to return a list which contains name
    of libraries mentioned in requirements.txt 
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:

        return requirement_file.readlines().remove("-e .")


# declaring variable for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.2"
AUTHOR = "Ganpat"
DESCRIPTION = "first ml prediction"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"
LICENSE = "Apache"
setup(
    name= PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),#["housing"]
    license=LICENSE,
    install_requires=get_requirements_list()
)


