import argparse, os
from .classes import Spritemaker

def main():
    parser = argparse.ArgumentParser(description="Spritemaker commandline")
    parser.add_argument('input', help='Input image')
    args = parser.parse_args()
    cwd = os.path.join(os.getcwd(), args.input)
    print(cwd)
    spritemaker = Spritemaker(cwd)
    spritemaker.show()