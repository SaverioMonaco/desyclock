from datetime import date, timedelta

from ..utils.sheet import Sheet


def main(args):
    s = Sheet()
    date_target = date.today() + timedelta(days=args.day)
    row = s.date_to_row(date_target)
    s.print_row(row)
