from pathlib import Path
from secrets import choice


def main():
    """Display a random nonempty quote from the bundled text file."""
    try:
        quotes = [line.strip() for line in Path(__file__).with_name("quotes.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
    except (OSError, UnicodeError):
        raise SystemExit("Unable to read quotes.txt.")
    if not quotes:
        raise SystemExit("No quotes available.")
    print(choice(quotes))


if __name__ == "__main__":
    main()
