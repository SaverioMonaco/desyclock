import sys
from datetime import date, datetime

from ..utils.print import success
from ..utils.sheet import Sheet


def main(args):
    # Use current year
    year = date.today().year

    day = args.day
    month = args.month

    # Check that day and month are provided
    if day is None or month is None:
        print("Error: Both --day and --month must be specified.")
        sys.exit(1)

    # Validate the date exists
    try:
        _ = date(year, month, day)
    except ValueError:
        print(f"Error: Invalid date {day}/{month}/{year}")
        sys.exit(1)

    # Check times argument
    if not args.times:
        print("Error: --times argument is required")
        sys.exit(1)

    times = args.times
    if len(times) % 2 != 0:
        print("Error: Times must be provided in start/end pairs")
        sys.exit(1)

    # Parse and validate all time strings
    parsed_times = []
    for t_str in times:
        try:
            t = datetime.strptime(t_str, "%H:%M").time()
            parsed_times.append(t)
        except ValueError:
            print(f"Error: Time '{t_str}' is not a valid HH:MM format.")
            sys.exit(1)

    # Validate times ordering
    for i in range(0, len(parsed_times), 2):
        start = parsed_times[i]
        end = parsed_times[i + 1]
        if start >= end:
            print(f"Error: Start time {start.strftime('%H:%M')} is not before end time {end.strftime('%H:%M')} in pair {i//2 + 1}.")
            sys.exit(1)

        # If there is a next pair, ensure no overlap (end <= next start)
        if i + 2 < len(parsed_times):
            next_start = parsed_times[i + 2]
            if end > next_start:
                print(f"Error: End time {end.strftime('%H:%M')} of pair {i//2 + 1} is after start time {next_start.strftime('%H:%M')} of next pair.")
                sys.exit(1)

    # Now proceed to write to sheet
    s = Sheet()
    date_target = date(year, month, day)
    row = s.date_to_row(date_target)

    # Clear existing work time cells for this row
    for work_column in s.WORK_COLUMNS:
        s.sheet.cell(row=row, column=work_column["start"]).value = None
        s.sheet.cell(row=row, column=work_column["end"]).value = None

    # Write the validated times to the sheet
    for i in range(0, len(parsed_times), 2):
        start_time = parsed_times[i]
        end_time = parsed_times[i + 1]
        start_cell = s.sheet.cell(row=row, column=s.WORK_COLUMNS[i // 2]["start"])
        end_cell = s.sheet.cell(row=row, column=s.WORK_COLUMNS[i // 2]["end"])

        start_cell.value = start_time
        start_cell.number_format = "HH:mm"
        end_cell.value = end_time
        end_cell.number_format = "HH:mm"

    s.save()
    success(f"Set work times for {date_target.strftime('%d/%m/%Y')}")
    s.print_row(row)