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
		#criar um dicionario com os aeroportos de destino para guardar as informações do número de vezes que cada um foi destino
		dic_aeroportos = {}
		for current, group in groupby(self, itemgetter(0)):
			total = 0 

			for item in group:
				total += item[1]
			
			dic_aeroportos[current] = total
		
		#pegar a info de qual foi o maior número de destinos e a partir disso achar no dicionário a key que corresponde a esse value
		max_dest = int(max(dic_aeroportos.values()))
		aeroporto = list(dic_aeroportos.keys())[list(dic_aeroportos.values()).index(max_dest)]

		self.emit(aeroporto, max_dest)

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
