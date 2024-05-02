import argparse, os
from .classes import Spritemaker

def main():
    parser = argparse.ArgumentParser(description="Spritemaker commandline")
    parser.add_argument('input', help='Input image')
    args = parser.parse_args()
    cwd = os.getcwd()
    print(cwd)
    spritemaker = Spritemaker(args.input)
    spritemaker.show()