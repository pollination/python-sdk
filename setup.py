# coding: utf-8

"""
    pollination-server

    Pollination Server OpenAPI Definition  # noqa: E501

    The version of the OpenAPI document: v0.17.0-staging
    Contact: info@pollination.cloud
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pollination-sdk"
VERSION = "v0.17.0-staging"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="pollination-server",
    author="PollinationSolutions",
    author_email="info@pollination.cloud",
    url="https://github.com/pollination/python-sdk",
    keywords=["OpenAPI", "OpenAPI-Generator", "pollination-server"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent"
    ],
)
