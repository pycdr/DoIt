#!/usr/bin/env python3
from json import load
from dicttoxml import dicttoxml
from os.path import exists
from sys import stderr

def _conv(d):
	out = ""
	for x in d:
		attrs = {}
		elems = {}
		text = ""
		for y in d[x]:
			if type(d[x][y]) == dict:
				elems[y] = d[x][y]
			elif type(d[x][y]) == list:
				for z in d[x][y]:
					text += "<%s>%s</%s>" % (y, z, y) # :P
			else: # str
				if y[0] == "@":
					attrs[y] = d[x][y]
				else: # starts with "#"
					text += d[x][y]
		out += "<%s" % x
		for y in attrs:
			out += " %s=\"%s\"" % (y[1::], attrs[y])
		out += ">"
		out += text
		out += _conv(elems)
		out += "</%s>" % x
	return out

def convert(path):
	# gets path of json file, then returns xml as string
	json = load(open(path, 'r'))
	out = _conv(json) # has the main algorithm
	return out

if __name__ == "__main__":
	# if you run program, it gets an argument from you as json file path
	from argparse import ArgumentParser
	parser = ArgumentParser(description="convert json to xml")
	parser.add_argument("path", help="the path of json file")
	args = parser.parse_args()
	path = args.path
	# check if file exists or not
	if not exists(path):
		print("error: please give an existing path!", file = stderr)
	# convert to xml
	out = convert(path)
	# print output
	print(out)
