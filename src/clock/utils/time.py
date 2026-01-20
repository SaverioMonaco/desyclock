from datetime import date, time

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def get_today_dict():
    today = date.today()
    return {
        "day": today.day,
        "month": today.month,
        "year": today.year,
    }

def format_timedelta(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"

def is_weekend(date_target):
    """Return True if it is a weekend"""
    return date_target.weekday() >= 5

def is_holiday(comment):
    return (comment is not None) and (comment not in MONTHS)

def time_to_minutes(t: time) -> int:
    return t.hour * 60 + t.minute


def minutes_to_time(m: int) -> time:
    m = max(0, min(23 * 60 + 59, int(m)))
    return time(m // 60, m % 60)