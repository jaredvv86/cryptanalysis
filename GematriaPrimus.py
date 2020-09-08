#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the functions for mapping Runic, Latin, and Positional info according the layout set out
in the GP
"""

## For start index of 0 choose start = 0 and stop = 29
## For start index of 1 choose start = 1 and stop = 30
start=0
stop=29
INTEGERS=[x for x in range(start,stop)]

RUNES=("ᚠ","ᚢ","ᚦ","ᚩ","ᚱ","ᚳ","ᚷ","ᚹ","ᚻ","ᚾ","ᛁ","ᛄ","ᛇ","ᛈ","ᛉ","ᛋ","ᛏ","ᛒ","ᛖ","ᛗ",
       "ᛚ","ᛝ","ᛟ","ᛞ","ᚪ","ᚫ","ᚣ","ᛡ","ᛠ")

PRIMES=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
        103,107,109)

LATIN=["F", "U","TH","O","R","K","G","W","H","N","I","J","EO","P","X","Z","T","B","E",
       "M","L","ING","OE","D","A","AE","Y","IA","EA"]

def prime_to_latin(prime):
    mapping = dict(zip(PRIMES, LATIN))
    return mapping[prime]

def latin_to_prime(latin):
    mapping = dict(zip(LATIN, PRIMES))
    return mapping[latin]

def prime_to_rune(prime):
	mapping = dict(zip(PRIMES, RUNES))
	return mapping[prime]

def rune_to_prime(rune):
    mapping = dict(zip(RUNES, PRIMES))
    return mapping[rune]

def rune_to_seq(rune):
    mapping = dict(zip(RUNES, INTEGERS))
    return mapping[rune]