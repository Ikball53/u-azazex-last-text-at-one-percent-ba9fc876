#!/usr/bin/env python3
"""Last Text at One Percent - the phone's own final message."""

from pathlib import Path


def craft_farewell() -> str:
    confession = "i autocorrected 'love you' to 'love ypu' 312 times and never told you"
    parting_sting = "your 6am alarm is still on"
    opener = "1%. confession: "
    closer = "good luck, human."
    return f"{opener}{confession}. {parting_sting}. {closer}"


def main() -> None:
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    farewell_text = craft_farewell()
    destination.write_bytes(farewell_text.encode("utf-8"))
    print(farewell_text)
    print(f"chars: {len(farewell_text)}")


if __name__ == "__main__":
    main()
