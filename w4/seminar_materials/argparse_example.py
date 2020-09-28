import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--number', help='Any number', default=-1)
parser.add_argument('-l', '--list', nargs=3, help='Any number', default=-1)
parser.add_argument('-p', help='Any number', default=-1)
parser.add_argument('--print', help='store_true example', action='store_true')
parser.add_argument('--const', help='store_const example', action='store_const', const=1)
parser.add_argument('pos_arg1')
parser.add_argument('pos_arg2')
# namespace.n or namespace.number

namespace = parser.parse_args()
if namespace.print:
    print(namespace)
