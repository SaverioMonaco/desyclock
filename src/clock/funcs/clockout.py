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

    # If you have not clocked in yet that day
    if not work_hours:
        error("Clock in first")
        return
    else:
        # Only check is to see if the last clock-in time is earlier that the clock out
        if not work_hours[-1]["end"] and datetime.combine(date.today(), work_hours[-1]["start"]) <= datetime.combine(date.today(), time):
            s.sheet.cell(row = row, column = s.WORK_COLUMNS[len(work_hours)-1]["end"]).value = time
            s.save()
            success("Clocked out at " + date_target.strftime('%d/%m/%Y') + " : " + time.strftime('%H:%M'))
            return
        else:
            error("Could not clock out")
            s.print_row(row)
            return


