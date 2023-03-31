#!/usr/bin/env python
import argparse
import re
import subprocess
from git import Repo

VERSION_FILE = "setup.py"
VERSION_REGEX = r"version=['\"](\d+\.\d+\.\d+)['\"]"


def bump_version(bump_type, commit=False, tag=False):
    with open(VERSION_FILE, "r") as f:
        contents = f.read()
        match = re.search(VERSION_REGEX, contents)

        if match:
            current_version = match.group(1)
            major, minor, patch = map(int, current_version.split("."))
            if bump_type == "major":
                major += 1
                minor = 0
                patch = 0
            elif bump_type == "minor":
                minor += 1
                patch = 0
            elif bump_type == "patch":
                patch += 1
            else:
                raise ValueError("Invalid bump type")
            new_version = f"{major}.{minor}.{patch}"
            new_contents = re.sub(VERSION_REGEX, f"version='{new_version}'", contents)

            with open(VERSION_FILE, "w") as f:
                f.write(new_contents)

            if commit or tag:
                repo = Repo(".")
                repo.index.add([VERSION_FILE])
                commit_message = (
                    f"Bumped version from {current_version} to {new_version}"
                )
                repo.index.commit(commit_message)

                if tag:
                    tag_name = f"v{new_version}"
                    repo.create_tag(tag_name)
                    print(f"Tagged as {tag_name}")

        else:
            raise ValueError(f"No version found in {VERSION_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Automatically bump the version in setup.py, optionally creating a commit and tag.")
    parser.add_argument(
        "bump_type",
        choices=["major", "minor", "patch"],
        help="The type of version bump",
    )
    parser.add_argument("--commit", action="store_true", help="Create a commit")
    parser.add_argument("--tag", action="store_true", help="Create a tag")
    args = parser.parse_args()

    bump_version(args.bump_type, commit=args.commit, tag=args.tag)


if __name__ == "__main__":
    main()
