from setuptools import setup, find_packages
import codecs
import os

DESCRIPTION = 'Tech-in-seconds'
LONG_DESCRIPTION = 'A package to genral and mathamathical operations'

# Setting up
setup(
    name="Tech-In-Seconds",
    author="Aadesh Lokhande",
    author_email="aadeshlokhande11@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['arithmetic', 'math', 'mathematics', 'tables','barakhadi','mean','contact', 'aadesh lokhande', 'tech in seconds', ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)