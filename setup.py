import os
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="rtm_doorstop",
    version="1.1.0",
    author="Andrew Simon",
    author_email="asimon1@protonmail.com",
    maintainer="Andrew Simon",
    maintainer_email="asimon1@protonmail.com",
    license="GNU GPL v3.0",
    url="https://github.com/scuriosity/rtm_doorstop",
    description="A tool to generate Requirement Traceability Matrices (RTMs) from Doorstop documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["rtm_doorstop"],
    python_requires=">=3.7",
    install_requires=["doorstop>=2.0.0", "rapidtables>=0.1", "fire>=0.3"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Software Development :: Quality Assurance",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points={"console_scripts": ["rtm_doorstop = rtm_doorstop:main"],},
)
