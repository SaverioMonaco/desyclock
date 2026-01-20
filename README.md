# DESYclock
Update the DESY time sheet file directly from terminal.

The script assumets that your file `Zeiterfassungstabelle YEAR Doktorand_innen.xlsx` is located in your `$HOME`.

## Installation
1. Move your file `Zeiterfassungstabelle 2026 Doktorand_innen.xlsx` in your home
2. Install the package
```bash
pip install git+https://github.com/SaverioMonaco/desyclock.git
```

## Usage

#### Clock-in and -out
By default, both clock in and out will write to the file the current time in the row of the current day, to change that you can use optional arguments:
- `-d` or `--day`: applies a shift in the day (e.g -1 is yesterday, 1 is tomorrow) (Default: 0)
- `-o` or `--hours`: applies a shift in the hour (Default: 0)
- `-m` or `--minutes`: applies a shift in the minutes (Default: 0)
* clock-in
```bash
clock in
```

* clock-out
```bash
clock out
```

You can also fill the cells of a specific day with specific times through the set command
```bash
clock set --day 20 --month 1 --times 9:30 13:30 14:30 18:30
```
- `-d` or `--day`: Specific day of the month
- `-m` or `--month`: Month
- `-t` or `--times`: Pairs of Clock-in and -outs

#### Print
You can print a row to see if everything is alright, by default it prints today's row, you can change that through:
- `-d` or `--day`: applies a shift in the day (e.g -1 is yesterday, 1 is tomorrow) (Default: 0)
```bash
clock print
```

#### Clear
You can clear a row. By default it clears today's row, you can change that through:
- `-d` or `--day`: applies a shift in the day (e.g -1 is yesterday, 1 is tomorrow) (Default: 0)
```bash
clock clear
```

#### Check
You can check from the start of the year until today if each entry is alright:
```bash
clock check
```