import argparse

from . import funcs


def main():
    parser = argparse.ArgumentParser(prog="clock")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # helloworld command
    hw_parser = subparsers.add_parser("helloworld", help="Print hello world")
    hw_parser.set_defaults(func=funcs.helloworld.main)

    # clock-in command
    clockin_parser = subparsers.add_parser("in", help="Clock in")
    clockin_parser.add_argument(
        "-m", "--minutes",
        type=int,
        default=0,
        help="Number of minutes to clock in (default: 0)"
    )
    clockin_parser.add_argument(
        "-h", "--hours",
        type=int,
        default=0,
        help="Number of hours to clock out (default: 0)"
    )
    clockin_parser.add_argument(
        "-d", "--day",
        type=int,
        default=0,
        help="Number of days to clock in (default: 0)"
    )
    clockin_parser.set_defaults(func=funcs.clockin.main)

    # clock-out command
    clockout_parser = subparsers.add_parser("out", help="Clock out")
    clockout_parser.add_argument(
        "-m", "--minutes",
        type=int,
        default=0,
        help="Number of minutes to clock out (default: 0)"
    )
    clockout_parser.add_argument(
        "-h", "--hours",
        type=int,
        default=0,
        help="Number of hours to clock out (default: 0)"
    )
    clockout_parser.add_argument(
        "-d", "--day",
        type=int,
        default=0,
        help="Number of days to clock out (default: 0)"
    )
    clockout_parser.set_defaults(func=funcs.clockout.main)

    # print row command
    print_parser = subparsers.add_parser("print", help="Print")
    print_parser.add_argument(
        "-d", "--day",
        type=int,
        default=0,
        help="Number of days to print (default: 0)"
    )
    print_parser.set_defaults(func=funcs.printrow.main)

    # check rows command
    check_parser = subparsers.add_parser("check", help="Check sanity of rows")
    check_parser.set_defaults(func=funcs.check.main)

    # clear row command
    clear_parser = subparsers.add_parser("clear", help="Clear row work hours")
    clear_parser.add_argument(
        "-d", "--day",
        type=int,
        default=0,
        help="Shift in number of days (default: 0)"
    )
    clear_parser.set_defaults(func=funcs.clear.main)

    args = parser.parse_args()
    args.func(args)
    
    