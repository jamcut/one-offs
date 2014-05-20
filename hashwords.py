#!/usr/bin/env python

import argparse
import hashlib

def hashthings(words, outfile, alg, verbose):
	print('[*] Using the {0} algorithm').format(alg)
	for word in words:
		word = word.strip()
		if word == '':
			continue
		else:
			hsh = hashlib.new(alg, word).hexdigest()
			if verbose == True:
				print('[*] {0} {1}').format(hsh, word)
			outfile.write(hsh + '\n')
	print('[*] {0} hashes written to {1}').format(str(len(words)), outfile.name)
	outfile.close()

parser = argparse.ArgumentParser(description='Calculate hashes for words')
parser.add_argument('-w', '--wordlist', help='file containing words to be hashed', required=True)
parser.add_argument('-f', '--file', help='file to write results to', required=True)
parser.add_argument('-a', '--algorithm', help='hashing algorithm to use', choices=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'], default='md5')
parser.add_argument('-v', '--verbose', help='show verbose output', action='store_true')

args = parser.parse_args()

words = open(args.wordlist, 'r').readlines()
outfile = open(args.file, 'w')
alg = args.algorithm
verbose = args.verbose

hashthings(words, outfile, alg, verbose)
