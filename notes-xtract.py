#!/usr/bin/env python

shortNames = []
HTTPPasswords = []
fileLines = open('notesfile.txt', 'r').readlines()

for line in fileLines:
	if '"ShortName"' in line:
		shortNames.append(line)

for line in fileLines:
	if '"HTTPPassword"' in line:
		HTTPPasswords.append(line)

outFile = open('notesout.txt', 'w')
maxCounter = len(shortNames)
counter = 0
while counter <= maxCounter:
	outFile.write(shortNames[counter]+"\n")
	outfile.write(HTTPPasswords[counter]+"\n")
	counter += 1
outFile.close()
