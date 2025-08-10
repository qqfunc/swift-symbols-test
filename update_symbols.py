"""Update SF Symbols."""

import plistlib
import sys
from pathlib import Path

PACKAGE_FILE = Path(__file__).parent / "Sources/Symbols/Symbol.swift"

SF_SYMBOLS_PATH = Path("/Applications/SF Symbols.app")
SF_SYMBOLS_METADATA_PATH = SF_SYMBOLS_PATH / "Contents/Resources/Metadata"
SF_SYMBOLS_NAME_AVAILABILITY_PATH = (
    SF_SYMBOLS_METADATA_PATH / "name_availability.plist"
)


def main() -> None:
    """Update SF Symbols."""
    if not PACKAGE_FILE.is_file():
        sys.exit(f"ERROR: Package file {PACKAGE_FILE.name} is not found.")

    if not SF_SYMBOLS_PATH.is_dir():
        sys.exit("ERROR: SF Symbols is not installed.")

    with SF_SYMBOLS_NAME_AVAILABILITY_PATH.open("rb") as plist_file:
        data = plistlib.load(plist_file)

    availabilities = {
        year: generate_availability(releases)
        for year, releases in data["year_to_release"].items()
    }

    cases = [
        f"{availabilities[year]}\n{generate_case(name)}"
        for name, year in data["symbols"].items()
    ]

    # TODO: Mark nonexhaustive: SE-0487 (Nonexhaustive enums).
    enum_statement = (
        "// This file is generated automatically. Do not edit.\n\n"
        "public enum Symbol: String {\n\n"
        f"{"\n\n".join(cases)}\n\n"
        "}\n\nextension Symbol: CaseIterable {}\n"
    )

    PACKAGE_FILE.write_text(enum_statement)


def generate_availability(releases: dict[str, str]) -> str:
    """Generate availability string."""
    releases = ", ".join(f"{os} {ver}" for os, ver in releases.items())
    return f"    @available({releases}, *)"


def generate_case(name: str) -> str:
    """Generate case string."""
    return f'    case `{name}` =  "{name}"'


if __name__ == "__main__":
    main()
