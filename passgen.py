#!/usr/bin/env python
"""
Functions for generating string(s) of chars.
"""

from random import choice

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def passgen(lenght=8):
    charseq = 0
    password = ''
    while charseq < lenght:
        password += choice(chars)
        charseq += 1
    return password

def passlistgen(lenght=8, count=1):
    passes = []
    passcount = 0
    while passcount < count:
        passes.append(passgen(lenght=lenght))
        passcount += 1
    return passes
