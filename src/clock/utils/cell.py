from datetime import date, datetime


def is_date(cell):
    return isinstance(cell.value, (date, datetime))