# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import sys
import glob

tsv = open("Results.tsv", 'w')

path = '../profilingCallsCacheHM/15_09/04'

for filename in glob.glob(os.path.join(path, '*.csv')):
	print filename
	
	f = open(filename, 'r')
	lines = f.readlines()
	print >> tsv, filename + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
	for item in lines[1279:1289]:
		print >> tsv, item.strip('\n')
	f.close
tsv.close
