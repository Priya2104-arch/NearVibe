import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "registrations.json"


def load_registrations():
    """Load saved registrations from the JSON file."""

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        return []


def save_registration(registration):
    """Save a new registration if it is not a duplicate."""

    registrations = load_registrations()

    email = registration["email"].strip().casefold()
    event_id = registration["event_id"]

    for existing in registrations:
        if (
            existing["email"].strip().casefold() == email
            and existing["event_id"] == event_id
        ):
            return False

    registrations.append(registration)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(registrations, file, indent=4)

    return True