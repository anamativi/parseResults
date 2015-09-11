# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import sys
import glob
path = '../profilingCallsCacheHM/15_09/04'
mode = sys.argv[1]

class Function:
	def __init__(self, name, lista):
		self.name = name
		self.Ir		= int(str(lista[0]).replace(',', ''))
		self.Dr		= int(str(lista[1]).replace(',', ''))
		self.Dw		= int(str(lista[2]).replace(',', ''))
		self.I1mr	= int(str(lista[3]).replace(',', ''))
		self.D1mr	= int(str(lista[4]).replace(',', ''))
		self.D1mw	= int(str(lista[5]).replace(',', ''))
		self.ILmr	= int(str(lista[6]).replace(',', ''))
		self.DLmr	= int(str(lista[7]).replace(',', ''))
		self.DLmw	= int(str(lista[8]).replace(',', ''))
		self.Dmw	= self.D1mw + self.DLmw
		self.Dwh	= self.Dw - self.Dmw		#data write hits only
		self.Dmr	= self.D1mr + self.DLmr	#total data read misses
		self.Drh	= self.Dr - self.Dmr		#data read hits only
		self.Imr	= self.I1mr + self.ILmr	#total instruction read misses
		self.Irh	= self.Ir - self.Imr		#instruction read hits only
		self.L1Rate	= 0.0
		self.I1Rate	= 0.0
		self.D1Rate	= 0.0
		self.LLRate	= 0.0
		self.ILRate	= 0.0
		self.DLRate	= 0.0
		
	def calcRates(self):
		if (self.Ir == 0 or self.Dr == 0 or self.Dw == 0):
			self.L1Rate	= 0
			self.I1Rate	= 0
			self.D1Rate	= 0
			self.LLRate	= 0
			self.ILRate	= 0
			self.DLRate	= 0
		else:
			self.L1Rate	= (self.I1mr + self.D1mr + self.D1mw) / ((self.Ir + self.Dr + self.Dw) * 0.01)
			self.I1Rate	= (self.I1mr) / ((self.Ir)* 0.01)
			self.D1Rate	= (self.D1mr + self.D1mw) / ((self.Dr + self.Dw)* 0.01)
			self.LLRate	= (self.ILmr + self.DLmr + self.DLmw) / ((self.Ir + self.Dr + self.Dw)* 0.01)
			self.ILRate	= (self.ILmr) / ((self.Ir) *0.01)
			self.DLRate	= (self.DLmr + self.DLmw) / ((self.Dr + self.Dw)* 0.01)	

	def toString(self):
		return self.name + '\t' + str(self.Ir) + '\t' + str(self.Dr) + '\t' + str(self.Dw) + '\t' + str(self.I1mr) + '\t' + str(self.D1mr) + '\t' + str(self.D1mw) + '\t' + str(self.ILmr) + '\t' + str(self.DLmr) + '\t' + str(self.DLmw) + '\t' + str(self.Irh) + '\t' + str(self.Drh) + '\t' + str(self.Dwh) + '\t' + str(self.L1Rate) + ' %\t' + str(self.I1Rate) + ' %\t' + str(self.D1Rate) + ' %\t' + str(self.LLRate) + ' %\t' + str(self.ILRate) + ' %\t' + str(self.DLRate) + ' %'


if mode == "txt":
	tsv = open("DetailedResults.tsv", 'w')

	for filename in glob.glob(os.path.join(path, '*.csv')):
		print filename
	
		f = open(filename, 'r')
		lines = f.readlines()
		print >> tsv, filename + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
		for item in lines[1279:1290]:
			print >> tsv, item.strip('\n')
		f.close
	tsv.close
else:
	if mode == "csv":
			tsv = open("CacheResults.tsv", 'w')
			print >> tsv, "Cache Configuration\tInstruction Read\tData Read\tData Write\t L1 Instruction Misses (Read)\tL1 Data Misses (Read)\tL1 Data Misses (Write)\tLL Instruction Misses (Read)\tLL Data Misses (Read)\tLL Data Misses (Write)\tIntruction Hits (Read)\tData Hits (Read)\tData Hits(Write)\tL1 Miss Rate\tL1 Instruction Miss Rate\tL1 Data Miss Rate\tLL Miss Rate\tLL Instruction Miss Rate\tLL Data Miss Rate"
			
			for filename in glob.glob(os.path.join(path, '*.txt')):
				if "annotate" in filename:
					print filename
					f = open(filename, 'r')
					lines = f.readlines()
					words = lines[20].split()
					
					name = filename.split('/')
					name = name[4].split("annotate_BasketballPass__QP_32_nF_8_")
					name = name[1]
					
					total = Function(name, words)
					total.calcRates()
					print >> tsv, total.toString()
					f.close
	tsv.close

