import argparse
parser = argparse.ArgumentParser(prog='toy',description = 'skynet creator',epilog = 'skynet has killed everyone', usage = '%(prog)s [lst]')
parser.add_argument('--foo',help='foo of the %(prog)s help')
parser.add_argument('bar', nargs='+', help='bar help')
args = parser.parse_args()
parser.print_help()
 
