#!/usr/bin/python
# -*- coding:utf-8 -*-

def isCheck(line):
	b_count = line.count('B')
	return b_count >= len(line) / 2 and b_count + 1 < len(line) 

def solution():
	with open('leapfrog_ch__sample_input.txt', 'r') as f:
		lines = f.readlines()
	for idx, line in enumerate(lines[1:]):
		print "Case #%d : %s" % (idx + 1, "Y" if isCheck(line.strip()) == True else "N")

def main():
	solution()

if __name__ == '__main__':
	main()
