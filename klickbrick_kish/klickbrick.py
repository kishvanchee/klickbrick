#!/usr/bin/env python3

import argparse
import sys


def parse(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('hello', default='Hello', help='Str for hello')
    parser.add_argument('-n', '--name', default='World', help='Optional arg for displaying name')
    return parser.parse_args(args)

def main():
    args = parse(sys.argv[1:])

    if args.hello == 'hello':
        print(f'{args.hello} {args.name}')


if __name__ == '__main__':
    main()
