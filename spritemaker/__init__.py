import argparse
from .classes import Spritemaker

def main():
    parser = argparse.ArgumentParser(description="Spritemaker commandline")
    parser.add_argument('-i', '--input', required=True, help='Input image')
    args = parser.parse_args()
    spritemaker = Spritemaker(args.input)
    spritemaker.show()