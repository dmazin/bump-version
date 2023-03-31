# bump-version

Automatically bump the version in setup.py, optionally creating a commit and tag.

## Installation

```bash
pip install bump-version
```

## Usage

```bash
usage: bump-version [-h] [--commit] [--tag] {major,minor,patch}

positional arguments:
  {major,minor,patch}  The type of version bump

options:
  -h, --help           show this help message and exit
  --commit             Create a commit
  --tag                Create a tag
```
