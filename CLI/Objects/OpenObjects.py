import npyscreen as nps
import os
import json

class RecentlyOpened(nps.BoxTitle):
	def create(self):
		self.values = [
			"["+x.split(",")[1]+"]: "+x.split(",")[0]
			for x in open("recently_opened",'r').read().split("\n")
			if(not x=="")and(not x.isspace())
		]

class NamesPaths(nps.BoxTitle):
	def create(self):
		self.names_dict = json.load(open("set_path.json",'r'))
		self.values = [
			x+" : "+self.names_dict[x]
			for x in self.names_dict
		]

class OpenForm(nps.FormBaseNew):
	def create(self):
		y,x = self.useable_space()
		self.form1 = self.add(
			RecentlyOpened, name="recently opened files",
			relx=0, rely=0, 
			max_width=x//2-1, max_height=(y)//2
		)
		self.form1.create()
		self.form2 = self.add(
			NamesPaths, name="saved paths",
			relx=x//2-1, rely=0,
			max_width=x//2-1, max_height=(y)//2
		)
		self.form2.create()
