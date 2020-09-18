#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image


def main():
	im = Image.open("01.jpg")
	hist_data = im.getcolors(maxcolors=256*256*256)
	for x in hist_data:
		print(x)

if __name__ == '__main__':
	main()