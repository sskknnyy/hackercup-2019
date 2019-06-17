#!/usr/bin/python
# -*- coding:utf-8 -*-

def isCheck(line):
	b_count = line.count('B')
	return b_count >= 2 and b_count + 1 < len(line) or (b_count == 1 and len(line) == 3)

def solution():
	with open('leapfrog_ch_.txt', 'r') as f:
		lines = f.readlines()
	outfile = open('leapfrog_ch2_output.txt', 'w')
	for idx, line in enumerate(lines[1:]):
		outfile.write("Case #%d: %s\n" % (idx + 1, "Y" if isCheck(line.strip()) == True else "N"))
	outfile.close()

def main():
	solution()

if __name__ == '__main__':
	main()
