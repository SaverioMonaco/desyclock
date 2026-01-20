import argparse

from . import funcs


def main():
    parser = argparse.ArgumentParser(prog="clock")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # helloworld command
    hw_parser = subparsers.add_parser("helloworld", help="Print hello world")
    hw_parser.set_defaults(func=funcs.helloworld.main)


    args = parser.parse_args()
    args.func(args)