import argparse

def calcs(args: argparse.Namespace):
    x = args.x
    y = args.y
    print(x+y)

root = argparse.ArgumentParser(description="Cli App")

subparse = root.add_subparsers(title="subapps", description='suba', required=True)

calc = subparse.add_parser("calc", help="Calculates numbers")
calc.add_argument("x", type=int)
calc.add_argument("y", type=int)
calc.add_argument("--verbose", default=False, action="store_true")
calc.set_defaults(func=calcs)

hello = subparse.add_parser("test", help="Just a test app")
hello.add_argument("w", type=str)

args = root.parse_args()
args.func(args)