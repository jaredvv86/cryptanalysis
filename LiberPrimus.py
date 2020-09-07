#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""define pages in the LP that can be imported and used for research
"""
import GematriaPrimus as GP

page40="""ᚠᚾᛗᚣᚷᛞᚫᚻᚪᛈᛉᚣᚻᛇᛠᚩᛖᛏᛝᛠᛚᛁᛏᚦᚠᛗᚪᚳᛖᛞᚳᛏᚱᛟᚷᛠᚾᚫᛒᚢᛖᛒᚢᚦᚠᛟᚷᛋᛟᛁᛈᛟᛉᛋᛒᚹᛄᛒᚣᛗᚢᛠᚱᛁᚢᛟᛄᛁᛗᛖᚫᚱᛋᛉᛝᛠᛈᛚᛞᚩᛚᛁᛉᛠᛝᛖᚱᚾᛈᛖᚹᛡᚾᛄᛏᚣᛋᚩᛋᛏᛝᚢᚾᛇᚪᛖᛏᚪᛄᚳᚣᛟᛒᛚᛋᛒᛞᛄᛁᛝᚣᛖᚳᛄᚻᛚᚣᚷᚫᛚᛞᛚᚫᛚᚦᛉᛚᛖᛉᚩᛉᛁᚳᚢᛗᚾᚢᚩᚾᛇᚻᛡᛚᛇᚩᚫᚪᚩᛟᚩᚣᚱᛖᚠᚢᛁᚻᛟᛚᚾᛏᚠᛞᚱᛠᚷᛈᚩᛇᚩᛗᛠᛒᛄᛡᛋᛗᚠᛏᚠᚫᚩᛟᚳᛚᛞᛡᛚᚩᚳᛝᚢᛈᚹᛏᚷᚳᛋᚢᛟᚷᚦᚠᛉᚠᛏᚳᛋᛉᛟᚷᚠᛉᚾᛞᛒᛏᛠᛡᛈᛡ"""

class Page:
	"""defines a Page object from the LP requires the rune text and the LP page number"""
	def __init__(self, rune_text, page_number):
		self.rune_text = rune_text
		self.page_number = page_number

	def rune_to_prime(self,):
		return [GP.rune_to_prime(rune) for rune in self.rune_text]

p40=Page(page40, 40)
print(p40.rune_to_prime())