#!/usr/bin/env python3
from xmltodict import parse
from json import dumps
from os.path import exists
from sys import stderr

def convert(path):
	# gets path of xml file, then returns json as string
	xml = open(path, 'r').read()
	dic = parse(xml)
	out = dumps(dic)
	return out

if __name__ == "__main__":
	# if you run program, it gets an argument from you as xml file path
	from argparse import ArgumentParser
	parser = ArgumentParser(description="convert xml to json")
	parser.add_argument("path", help="the path of xml file")
	args = parser.parse_args()
	path = args.path
	# check if file exists or not
	if not exists(path):
		print("error: please give an existing path!", file = stderr)
	# convert to json
	out = convert(path)
	# print output
	print(out)
