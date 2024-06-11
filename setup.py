"""(C) 2013-2024 Copycat Software, LLC. All Rights Reserved."""

import os
import re

from os import path
from setuptools import (
    find_packages,
    setup)


PROJECT_PATH = path.abspath(path.dirname(__file__))
VERSION_RE = re.compile(r"""__version__ = [""]([0-9.]+((dev|rc|b)[0-9]+)?)[""]""")


with open(os.path.join(os.path.dirname(__file__), "README.rst"), encoding="utf-8") as readme:
    README = readme.read()


def get_version():
    """Get Version."""
    init = open(path.join(PROJECT_PATH, "scaffolding", "__init__.py"), encoding="utf-8").read()

    return VERSION_RE.search(init).group(1)


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name="ddaemon-infra",
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    license="GPLv3 License",
    description="DDaemon Infrastructure.",
    long_description=README,
    url="https://github.com/asuvorov/ddaemon-infra/",
    author="Artem Suvorov",
    author_email="artem.suvorov@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPLv3 License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9.6",
    ],
    install_requires=[
        # Your Package Dependencies go here.
    ],
    test_suite="nose.collector",
    tests_require=["nose"],
)
