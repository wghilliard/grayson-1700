from setuptools import setup, find_packages

version = open("VERSION").read().strip()

with open("requirements.txt", encoding="utf8") as handle:
    reqs = handle.readlines()

with open("requirements-dev.txt", encoding="utf8") as handle:
    dev_reqs = handle.readlines()

setup(
    name="wgh-ner",
    version=version,
    author="Grayson Hilliard",
    author_email="grsn.hilliard@gmail.com",
    url="",
    description="",
    long_description=open("README.md").read(),
    classifiers=[
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],
    packages=find_packages("ner"),
    install_requires=reqs,
    extras_require={
        "dev": dev_reqs,
    },
    platforms="any",
)
