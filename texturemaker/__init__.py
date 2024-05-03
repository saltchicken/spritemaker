import argparse, os
from .classes import Texturemaker

def main():
    parser = argparse.ArgumentParser(description="Spritemaker commandline")
    parser.add_argument('input', help='Input image')
    args = parser.parse_args()
    texturemaker = Texturemaker(args.input)
    texturemaker.resize()
    texturemaker.save()
