from datetime import date

from rich.console import Console
from rich.live import Live

from ..utils.print import warn
from ..utils.sheet import Sheet
from ..utils.time import is_holiday, is_weekend

console = Console()

def main(args):
    s = Sheet()
    today = date.today()
    today_row = s.date_to_row(today)

    with Live(console=console, refresh_per_second=4) as live:
        for row in range(s.DATE_ROW_FIRST, today_row + 1):
            date_target = s.sheet.cell(row=row, column=s.DATE_COLUMN).value
            live.update(f"[green]Checking[/green] {date_target.strftime('%d/%m/%Y')} | Row: {row}")

            total_time, work_hours = s.get_work_hours(row, verbose=True)

            comment = s.sheet.cell(row=row, column=s.COMMENT_COLUMN).value
            if work_hours and (is_holiday(comment) or is_weekend(date_target)):
                warn(f"({date_target.strftime('%d/%m/%Y')}) You worked on a holiday or a weekend")