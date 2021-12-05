#!/usr/bin/env python3

import sys

from itertools import groupby
from operator import itemgetter

SEP = "\t"

class Reducer(object):

	def __init__(self, infile=sys.stdin, separator=SEP):
		self.infile = infile
		self.sep = separator

	def emit(self, key, value):
		sys.stdout.write(f"{key}{self.sep}{value}\n")

	def reduce(self):
		for current, group in groupby(self, itemgetter(0)):
			dic_voos = {}
			dic_max_voo = {}

			for item in group:
				if item[1] in dic_voos:
					dic_voos[item[1]] += 1
				else:
					dic_voos[item[1]] = 1
			
			max_voo = int(max(dic_voos.values()))
			voo = int(list(dic_voos.keys())[list(dic_voos.values()).index(max_voo)])
			dic_max_voo[voo] = max_voo

			self.emit(current, dic_max_voo)

	def __iter__(self):
		for line in self.infile:
			try:
				parts = line.split(self.sep)
				yield parts[0], float(parts[1])
			except:
				continue

if __name__ == '__main__':
	reducer = Reducer(sys.stdin)
	reducer.reduce()
