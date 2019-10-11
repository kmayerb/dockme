
import sys
from dockme.transform import _log10_transform
import argparse
parser = argparse.ArgumentParser(description='Log10 Transform a Numeric Value')

parser.add_argument('--input', type=str, help='supply filename with numeric values one per line', default = "input.txt")
parser.add_argument('--output', type=str, help='supply filename for output file', default = "output.txt")

args =  parser.parse_args()
fh = open(args.input, "r")
values = [float(x.strip()) for x in fh.readlines()]
fh.close()

tranformed_values = [_log10_transform(x) for x in values]
oh = open(args.output, "w")

for v, tv in zip(values, tranformed_values):
	oh.write('{}\t{}\n'.format(v,tv))
	print('{}\t{}\n'.format(v,tv))

oh.close()



