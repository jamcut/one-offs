#!/usr/bin/env python

hashpassdict = {}
userhashdict = {}

hashpass = open('hashpass.txt', 'r').readlines()
userhash = open('userhash.txt', 'r').readlines()

for line in userhash:
	line = line.split(':')
	userhashdict[line[0]] = line[1]

for line in hashpass:
	line =  line.split(':')
	hashpassdict[line[0]] = line[1]

counter = 0
finaldict = userhashdict

for hk, hv in hashpassdict.iteritems():
	for uk, uv in userhashdict.iteritems():
#		print("Comparing " + hk + " and " + uv + "\n")
		if hk.strip() == uv.strip():
			finaldict[uk] = hv
			counter += 1
		else:
			continue
outfile = open('user_pass.txt', 'w')

for k, v in finaldict.iteritems():
	outfile.write(k + ":" + v + "\n")
print("matched " + str(counter) + " items")