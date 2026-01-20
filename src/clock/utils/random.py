import random
from datetime import time

from .time import minutes_to_time, time_to_minutes


def gaussian_minutes(mean: int, sigma: float) -> int:
    return int(random.gauss(mean, sigma))

def generate_day_times(
    mean_arrival=time(9, 0),
    sigma_arrival=20,
    mean_leave=time(18, 0),
    sigma_leave=30,
    lunch_start=time(12, 30),
    lunch_mean_duration=30,
    lunch_sigma=5,
):
    """
    Returns:
        arrival, lunch_start, lunch_end, leave
    """

    lunch_start_min = time_to_minutes(lunch_start)

    # --- Arrival (must be before lunch)
    while True:
        arrival_min = gaussian_minutes(
            time_to_minutes(mean_arrival),
            sigma_arrival,
        )
        if arrival_min < lunch_start_min - 30:  # at least some work before lunch
            break

    # --- Lunch duration (>= 15 min)
    lunch_duration = max(
        15,
        gaussian_minutes(lunch_mean_duration, lunch_sigma),
    )

    lunch_end_min = lunch_start_min + lunch_duration

    # --- Leave (must be after lunch)
    while True:
        leave_min = gaussian_minutes(
            time_to_minutes(mean_leave),
            sigma_leave,
        )
        if leave_min > lunch_end_min + 60:  # at least 1h after lunch
            break

    return (
        minutes_to_time(arrival_min),
        lunch_start,
        minutes_to_time(lunch_end_min),
        minutes_to_time(leave_min),
    )
