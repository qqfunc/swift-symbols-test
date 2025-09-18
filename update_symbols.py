"""Update SF Symbols."""

import plistlib
import sys
from pathlib import Path

SOURCE_DIR = Path(__file__).parent / "Sources/SFSymbols"
SFSYMBOL_FILE = SOURCE_DIR / "SFSymbol.swift"

SF_SYMBOLS_PATH = Path("/Applications/SF Symbols.app")
SF_SYMBOLS_METADATA_PATH = SF_SYMBOLS_PATH / "Contents/Resources/Metadata"
SF_SYMBOLS_NAME_AVAILABILITY_PATH = (
    SF_SYMBOLS_METADATA_PATH / "name_availability.plist"
)

FILE_HEADER = "// This file is generated automatically. Do not edit.\n\n"


def main() -> None:
    """Update SF Symbols."""
    if not SFSYMBOL_FILE.is_file():
        sys.exit(f"ERROR: Package file {SFSYMBOL_FILE.name} is not found.")

    if not SF_SYMBOLS_PATH.is_dir():
        sys.exit("ERROR: SF Symbols is not installed.")

    with SF_SYMBOLS_NAME_AVAILABILITY_PATH.open("rb") as plist_file:
        data = plistlib.load(plist_file)

    availabilities: dict[str, str] = {
        year: generate_availability(releases)
        for year, releases in data["year_to_release"].items()
    }

    symbols: dict[str, str] = data["symbols"].items()

    write_symbol_file(symbols, availabilities)


def write_symbol_file(
    symbols: dict[str, str],
    availabilities: dict[str, str],
) -> None:
    """Write ``SFSymbol+Symbols.swift`` file."""
    (SOURCE_DIR / "SFSymbol+Symbols.swift").write_text(
        FILE_HEADER
        + "public extension SFSymbol {\n\n"
        + "".join(
            [
                availabilities[year] + generate_symbol_definition(name)
                for name, year in symbols
            ],
        )
        + "}\n",
    )


def generate_availability(releases: dict[str, str]) -> str:
    """Generate availability string."""
    releases = ", ".join(f"{os} {ver}" for os, ver in releases.items())
    return f"    @available({releases}, *)\n"


def generate_symbol_definition(name: str) -> str:
    """Generate static let string."""
    return f'    static let `{name}` = SFSymbol(name: "{name}")\n\n'


if __name__ == "__main__":
    main()
