"""
Generate random clock in and outs because why not
"""

from datetime import date, time

from rich.console import Console
from rich.live import Live

from ..utils.print import success
from ..utils.random import generate_day_times
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
            live.update(f"[green]Generating[/green] {date_target.strftime('%d/%m/%Y')} | Row: {row}")

            total_time, work_hours = s.get_work_hours(row, verbose=True)
            comment = s.sheet.cell(row=row, column=s.COMMENT_COLUMN).value
            if not work_hours:
                if (not is_holiday(comment) and not is_weekend(date_target)):   
                    arrival, lunch_start, lunch_end, leave = generate_day_times(
                        mean_arrival=time(args.h0, args.m0),
                        sigma_arrival=args.s0,
                        lunch_start=time(12, 30),
                        lunch_mean_duration=30,
                        lunch_sigma=args.sl,
                        mean_leave=time(args.h1, args.m1),
                        sigma_leave=args.s1
                    )

                    s.sheet.cell(row=row, column=s.WORK_COLUMNS[0]["start"]).value = arrival
                    s.sheet.cell(row=row, column=s.WORK_COLUMNS[0]["end"]).value = lunch_start
                    s.sheet.cell(row=row, column=s.WORK_COLUMNS[1]["start"]).value = lunch_end
                    s.sheet.cell(row=row, column=s.WORK_COLUMNS[1]["end"]).value = leave
                    
    s.save()

    success("Generated random times")