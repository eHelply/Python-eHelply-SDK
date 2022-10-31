"""
    eHelply SDK - 1.1.116

    eHelply SDK for SuperStack Services  # noqa: E501

    The version of the OpenAPI document: 1.1.116
    Contact: support@ehelply.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ehelply-python-sdk"
VERSION = "1.1.116"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="eHelply SDK - 1.1.116",
    author="Support",
    author_email="support@ehelply.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "eHelply SDK - 1.1.116"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    eHelply SDK for SuperStack Services  # noqa: E501
    """
)
