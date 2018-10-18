import argparse

import numpy as np

def hypotenuse(xs, ys):
    return np.sqrt(xs * xs + ys * ys)


def hypotenuse_main():
    parser = argparse.ArgumentParser(description='Computes a hypotenuse')
    parser.add_argument('base', type=float, help='Base of the triangle')
    parser.add_argument('height', type=float, help='Height of the triangle')
    args = parser.parse_args()
    print('Base:', args.base)
    print('Height:', args.height)
    print('Hypotenuse:', hypotenuse(np.array(args.base), np.array(args.height)))
