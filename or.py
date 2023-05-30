import argparse

parser = argparse.ArgumentParser(description="convert to from hex to or\nsee: https://developer.apple.com/library/archive/technotes/tn2450/_index.html for mac key usages")
parser.add_argument('val')
args = parser.parse_args()

def convert(val):
    int_val = int(val, 16)
    int_ref = 0x700000000

    return hex(int_ref | int_val)

print(convert(args.val))
