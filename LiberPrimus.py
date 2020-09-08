#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""define pages in the LP that can be imported and used for research
"""
import GematriaPrimus as GP

page40="""ᚠᚾᛗᚣᚷᛞᚫᚻᚪᛈᛉᚣᚻᛇᛠᚩᛖᛏᛝᛠᛚᛁᛏᚦᚠᛗᚪᚳᛖᛞᚳᛏᚱᛟᚷᛠᚾᚫᛒᚢᛖᛒᚢᚦᚠᛟᚷᛋᛟᛁᛈᛟᛉᛋᛒᚹᛄᛒᚣᛗᚢᛠᚱᛁᚢᛟᛄᛁᛗᛖᚫᚱᛋᛉᛝᛠᛈᛚᛞᚩᛚᛁᛉᛠᛝᛖᚱᚾᛈᛖᚹᛡᚾᛄᛏᚣᛋᚩᛋᛏᛝᚢᚾᛇᚪᛖᛏᚪᛄᚳᚣᛟᛒᛚᛋᛒᛞᛄᛁᛝᚣᛖᚳᛄᚻᛚᚣᚷᚫᛚᛞᛚᚫᛚᚦᛉᛚᛖᛉᚩᛉᛁᚳᚢᛗᚾᚢᚩᚾᛇᚻᛡᛚᛇᚩᚫᚪᚩᛟᚩᚣᚱᛖᚠᚢᛁᚻᛟᛚᚾᛏᚠᛞᚱᛠᚷᛈᚩᛇᚩᛗᛠᛒᛄᛡᛋᛗᚠᛏᚠᚫᚩᛟᚳᛚᛞᛡᛚᚩᚳᛝᚢᛈᚹᛏᚷᚳᛋᚢᛟᚷᚦᚠᛉᚠᛏᚳᛋᛉᛟᚷᚠᛉᚾᛞᛒᛏᛠᛡᛈᛡ"""

class Page(object):
	"""defines a Page object from the LP requires the rune text and the LP page number"""
	def __init__(self, rune_text, page_number=None):
		self.rune_text = rune_text
		self.page_number = page_number
		self.unique_chars = [char for char in set(self.rune_text)]

	def get_prime_form(self):
		
		#return [GP.rune_to_prime(rune) for rune in self.rune_text]

	def get_seq_form(self):
		return [GP.rune_to_seq(rune) for rune in self.rune_text]

	def get_unique_chars(self):
		return self.unique_chars

	def get_char_counts(self):
		pass

p40=Page(page40, 40)
#print(p40.get_prime_form())
#print(p40.get_seq_form())
print(p40.get_unique_chars().get_prime_form())