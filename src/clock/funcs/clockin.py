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

    if is_weekend(date_target):
        warn(f"{date_target} is a weekend")
    if is_holiday(comment):
        warn(f"{date_target} is a holiday")

    if not work_hours:
        s.sheet.cell(row = row, column = s.WORK_COLUMNS[0]["start"]).value = time
        s.save()
        success("Clocked in at " + date_target.strftime('%d/%m/%Y') + " : " + time.strftime('%H:%M'))
        return
    else:
        if not work_hours[-1]["end"]:
            error("Clock out first")
            s.print_row(row)
            return
        elif work_hours[-1]["end"] >= time:
            error("You cannot clock in before last clock out")
            s.print_row(row)
            return
        else:
            if len(work_hours) >= len(s.WORK_COLUMNS):
                error("You cannot clock in and out more than " + str(len(s.WORK_COLUMNS)) + " times a day")
                s.print_row(row)
                return
            else:
                s.sheet.cell(row = row, column = s.WORK_COLUMNS[len(work_hours)]["start"]).value = time
                s.save()
                success("Clocked in at " + date_target.strftime('%d/%m/%Y') + " : " + time.strftime('%H:%M'))
                return


