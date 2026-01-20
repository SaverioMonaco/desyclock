"""
Clear the work hours of a day in case you did an oopsie
"""
from datetime import date, timedelta

from ..utils.print import success
from ..utils.sheet import Sheet


def main(args):
    s = Sheet()
    date_target = date.today() + timedelta(days=args.day)
    row = s.date_to_row(date_target)
    
    for work_column in s.WORK_COLUMNS:
        # Set them to none
        s.sheet.cell(row = row, column = work_column["start"]).value = None
        s.sheet.cell(row = row, column = work_column["end"]).value = None    
    s.save()
    
    success(f"{date_target.strftime('%d/%m/%Y')} cleared")
