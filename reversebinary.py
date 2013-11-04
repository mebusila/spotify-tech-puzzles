#!/usr/bin/env python

__author__ = 'Serban Carlogea'
__email__ = 'sherban.carlogea@gmail.com'

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print int('{0:b}'.format(n)[::-1], 2)