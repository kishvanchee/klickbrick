#!/usr/bin/env python3

import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('hello', default='Hello', help='Str for hello')
    parser.add_argument('-n', '--name', default='World', help='Optional arg for displaying name')
    return parser

def main():
    parser = parse()
    args = parser.parse_args()

    if args.hello == 'hello':
        print(f'{args.hello} {args.name}')


if __name__ == '__main__':
    main()
