#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides the functions for mapping Runic, Latin, and Positional info according the layout set out
in the GP
"""

integers=[x for x in range(0,29)]
runes=("ᚠ","ᚢ","ᚦ","ᚩ","ᚱ","ᚳ","ᚷ","ᚹ","ᚻ","ᚾ","ᛁ","ᛄ","ᛇ","ᛈ","ᛉ","ᛋ","ᛏ","ᛒ","ᛖ","ᛗ",
       "ᛚ","ᛝ","ᛟ","ᛞ","ᚪ","ᚫ","ᚣ","ᛡ","ᛠ")
primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,
        103,107,109)
latin=["F", "U","TH","O","R","K","G","W","H","N","I","J","EO","P","X","Z","T","B","E",
       "M","L","ING","OE","D","A","AE","Y","IA","EA"]
def prime_to_latin(prime):
    mapping = dict(zip(primes, latin))
    return mapping[prime]

def latin_to_prime(latin):
    mapping = {
		"F": 2,
        "U": 3,
        "TH":5,
        "O": 7,
        "R":11,
        "K":13,
        "G":17,
        "W":19,
        "H":23,
        "N":29,
        "I":31,
        "J":37,
        "EO":41,
        "P":43,
        "X":47,
        "Z":53,
        "T":59,
        "B":61,
        "E":67,
        "M":71,
        "L":73,
        "ING":79,
        "OE":83,
        "D":89,
        "A":97,
        "AE":101,
        "Y":103,
        "IA":107,
        "EA":109}
    try:
        return mapping[latin]
    except KeyError as e:
            print(e," IS NOT IN THE MAPPING" )
            raise e

def prime_to_rune(prime):
    '''
    defines the mapping from primes runic charaters according to the GP.
    Raises an exception if the input is NOT prime
    '''
    mapping = {
        2:"ᚠ",
        3:"ᚢ",
        5:"ᚦ",
        7:"ᚩ",
        11:"ᚱ",
        13:"ᚳ",
        17:"ᚷ",
        19:"ᚹ",
        23:"ᚻ",
        29:"ᚾ",
        31:"ᛁ",
        37:"ᛄ",
        41:"ᛇ",
        43:"ᛈ",
        47:"ᛉ",
        53:"ᛋ",
        59:"ᛏ",
        61:"ᛒ",
        67:"ᛖ",
        71:"ᛗ",
        73:"ᛚ",
        79:"ᛝ",
        83:"ᛟ",
        89:"ᛞ",
        97:"ᚪ",
        101:"ᚫ",
        103:"ᚣ",
        107:"ᛡ",
        109:"ᛠ"}
    try:
        return mapping[prime]
    except KeyError as e:
        print(e," IS NOT IN THE MAPPING" )
        raise e	

def rune_to_prime(rune):
    mapping = dict(zip(runes, primes))
    return mapping[rune]

def rune_to_seq(rune,zero=False):
    '''
    defines the mapping from runic to sequential according to the GP.
    Raises an exception if the input is NOT prime
    '''
    if zero==False:
        z=0
    else:
        z=1
    mapping = {
        "ᚠ":1-z,
        "ᚢ":2-z,
        "ᚦ":3-z,
        "ᚩ":4-z,
        "ᚱ":5-z,
        "ᚳ":6-z,
        "ᚷ":7-z,
        "ᚹ":8-z,
        "ᚻ":9-z,
        "ᚾ":10-z,
        "ᛁ":11-z,
        "ᛄ":12-z,
        "ᛇ":13-z,
        "ᛈ":14-z,
        "ᛉ":15-z,
        "ᛋ":16-z,
        "ᛏ":17-z,
        "ᛒ":18-z,
        "ᛖ":19-z,
        "ᛗ":20-z,
        "ᛚ":21-z,
        "ᛝ":22-z,
        "ᛟ":23-z,
        "ᛞ":24-z,
        "ᚪ":25-z,
        "ᚫ":26-z,
        "ᚣ":27-z,
        "ᛡ":28-z,
        "ᛠ":29-z}
    try:
        return mapping[rune]
    except KeyError as e:
        print(e," IS NOT IN THE MAPPING" )
        raise e 