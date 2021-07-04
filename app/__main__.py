!/usr/local/bin python3

import click
import sys

def parse_args():

    '''Parse args and set the chosen sub-command as the default function.'''

    # main parser for command line arguments
    parser = argparse.ArgumentParser(
        description='Digital preservation utilities.'
        )
    subparsers = parser.add_subparsers(
        title='subcommands', description='valid subcommands', 
        help='-h additional help', metavar='{bc,inv,comp,ver}', dest='cmd'
        )
    parser.add_argument(
        '-v', '--version', action='version', help='Print version number and exit',
        version='%(prog)s 0.5'
        )
    subparsers.required = True

    # parser for the "bagcheck" sub-command
    bagcheck_parser = subparsers.add_parser(
        'bagcheck', aliases=['bck'],
        help='Compare an inventory file against a bagit bag',
        description='Checks relpath & checksum against bag manifest.'
        )
    bagcheck_parser.add_argument(
        '-i', '--inventory', help='Inventory CSV to compare', action='store'
        )
    bagcheck_parser.add_argument(
        '-b', '--bag', help='Path to BagIt bag', action='store'
        )
    bagcheck_parser.set_defaults(func=bagcheck)



    # parse the args and call the default sub-command function
    args = parser.parse_args()
    print_header(args.func.__name__)
    result = args.func(args)
    if result:
        sys.stderr.write(result)
        sys.stderr.write('\n\n')


def main():
    pass


if __name__ == "__main__":
    main()
