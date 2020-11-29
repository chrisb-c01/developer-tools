# Standard library imports
from datetime import datetime as dt

# Third party imports
from pytz import timezone

# Local application imports
from app.const import NAME

tz = timezone("Europe/Amsterdam")


def print_hi(name: str):
    if not isinstance(name, str):
        raise TypeError("name is of invalid type")
    if not len(name):
        raise ValueError("Please enter a valid name")
    date_time = tz.localize(dt.now())
    print(f"Hi, {name} it is currently {date_time}")


if __name__ == "__main__":
    print_hi(NAME)
