from setuptools import find_packages, setup

CLASSIFIERS = [
    "License :: OSI Approved :: BSD License",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]

setup(
    name="az-cli-wizard",
    version="0.0.1",
    description="A wizard for the Azure CLI",
    long_description=open("README.md").read(),
    author="Anthony Shaw",
    author_email="anthonyshaw@apache.org",
    url="https://github.com/tonybaloney/az-cli-wizard",
    license="MIT",
    packages=find_packages(),
    install_requires=["rich", "inquirer", "azure-cli"],
    classifiers=CLASSIFIERS,
    keywords="azure",
    entry_points={
        "console_scripts": ["az-wizard=azcliwizard.main:main"],
    },
)
