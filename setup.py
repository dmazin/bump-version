from setuptools import setup, find_packages

setup(
    name="bump-version",
    version='0.0.1',
    description="A command-line tool to automatically bump the version of a Python project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dmitry Mazin",
    author_email="dm@cyberdemon.org",
    url="https://github.com/dmazin/bump-version",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bump-version=bump_version.core:main",
        ],
    },
    install_requires=[
        "gitpython",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
