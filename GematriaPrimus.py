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
    '''
    defines a mapping from the primes to their latin char, according to the GP
    raises exception if input is NOT prime or in list
    '''
    
    mapping = {
        2:  ,
        3:  "U",
        5:  "TH",
        7:  "O",
        11: "R",
        13: "K",
        17: "G",
        19: "W",
        23: "H",
        29: "N",
        31: "I",
        37: "J",
        41: "EO",
        43: "P",
        47: "X",
        53: "Z",
        59: "T",
        61: "B",
        67: "E",
        71: "M",
        73: "L",
        79: "ING",
        83: "OE",
        89: "D",
        97: "A",
        101:"AE",
        103:"Y",
        107:"IA",
        109:"EA"}
    try:
        return mapping[prime]
    except KeyError as e:
        print(e," IS NOT IN THE MAPPING" )
        raise e

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
    '''
    defines the mapping from primes runic charaters according to the GP.
    Raises an exception if the input is NOT prime
    '''
    mapping = {
        "ᚠ":2,
        "ᚢ":3,
        "ᚦ":5,
        "ᚩ":7,
        "ᚱ":11,
        "ᚳ":13,
        "ᚷ":17,
        "ᚹ":19,
        "ᚻ":23,
        "ᚾ":29,
        "ᛁ":31,
        "ᛄ":37,
        "ᛇ":41,
        "ᛈ":43,
        "ᛉ":47,
        "ᛋ":53,
        "ᛏ":59,
        "ᛒ":61,
        "ᛖ":67,
        "ᛗ":71,
        "ᛚ":73,
        "ᛝ":79,
        "ᛟ":83,
        "ᛞ":89,
        "ᚪ":97,
        "ᚫ":101,
        "ᚣ":103,
        "ᛡ":107,
        "ᛠ":109}
    try:
        return mapping[rune]
    except KeyError as e:
        print(e," IS NOT IN THE MAPPING" )
        raise e	

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