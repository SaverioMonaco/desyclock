from pathlib import Path

from .time import get_today_dict

EXCEL_FILE = Path.home() / f"Zeiterfassungstabelle {get_today_dict()['year']} Doktorand_innen.xlsx"


def excel_file_exists():
    return (EXCEL_FILE).is_file()