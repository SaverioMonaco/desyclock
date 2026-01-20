"""
Clock in: 
Args:
    -d (int): Shift in days to today (default: 0)
    -h (int): Shift in hours to now (default: 0)
    -m (int): Shift in minutes to now (default: 0)
"""
from datetime import date, datetime, timedelta

from ..utils.print import error, success, warn
from ..utils.sheet import Sheet
from ..utils.time import is_holiday, is_weekend


def main(args):
    s = Sheet()
    date_target = date.today() + timedelta(days=args.day)
    row = s.date_to_row(date_target)
    comment = s.sheet.cell(row=row, column=s.COMMENT_COLUMN).value
    
    time = (datetime.now() + timedelta(minutes=args.minutes) + timedelta(hours=args.hours)).time()

    total_time, work_hours = s.get_work_hours(row)

    # Bruh, don't
    if is_weekend(date_target):
        warn(f"{date_target} is a weekend")
    if is_holiday(comment):
        warn(f"{date_target} is a holiday")

    # If you have no clocked in today
    if not work_hours:
        s.sheet.cell(row = row, column = s.WORK_COLUMNS[0]["start"]).value = time
        s.save()
        success("Clocked in at " + date_target.strftime('%d/%m/%Y') + " : " + time.strftime('%H:%M'))
        return
    else:
        # If you have not clocked out
        if not work_hours[-1]["end"]:
            error("Clock out first")
            s.print_row(row)
            return
        # If the clock in time is earlier than the last clock out time
        elif work_hours[-1]["end"] >= time:
            error("You cannot clock in before last clock out")
            s.print_row(row)
            return
        else:
            # If you run out of slots
            if len(work_hours) >= len(s.WORK_COLUMNS):
                error("You cannot clock in and out more than " + str(len(s.WORK_COLUMNS)) + " times a day")
                s.print_row(row)
                return
            else:
                s.sheet.cell(row = row, column = s.WORK_COLUMNS[len(work_hours)]["start"]).value = time
                s.save()
                success("Clocked in at " + date_target.strftime('%d/%m/%Y') + " : " + time.strftime('%H:%M'))
                return