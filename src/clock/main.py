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
        "-o", "--hours",
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
        "-o", "--hours",
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

    # set row command
    setrow_parser = subparsers.add_parser("set", help="Set row work hours")
    setrow_parser.add_argument(
        "-d", "--day",
        type=int,
    )
    setrow_parser.add_argument(
        "-m", "--month",
        type=int,
    )
    setrow_parser.add_argument(
    "-t", "--times",
    nargs="+",
    help="List of time arguments: TIME1_START TIME1_END TIME2_START TIME2_END ..."
    )
    setrow_parser.set_defaults(func=funcs.setrow.main)

    # set row command
    random_parser = subparsers.add_parser("random", help="Fill work hours")
    random_parser.add_argument(
        "--h0",
        type=int,
        default=9,
        help="Mean arrival hour (default: 9)"
    )
    random_parser.add_argument(
        "--m0",
        type=int,
        default=30,
        help="Mean arrival minute (default: 30)"
    )
    random_parser.add_argument(
        "--s0",
        type=int,
        default=10,
        help="Arrival sigma"
    )
    random_parser.add_argument(
        "--sl",
        type=int,
        default=10,
        help="Lunch sigma"
    )
    random_parser.add_argument(
        "--h1",
        type=int,
        default=18,
        help="Mean leave hour (default: 18)"
    )
    random_parser.add_argument(
        "--m1",
        type=int,
        default=30,
        help="Mean leave minute (default: 30)"
    )
    random_parser.add_argument(
        "--s1",
        type=int,
        default=20,
        help="leave sigma"
    )
    random_parser.set_defaults(func=funcs.random.main)

    args = parser.parse_args()
    args.func(args)
    
    