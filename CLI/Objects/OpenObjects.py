import npyscreen as nps
import os
import json
import curses
from curses import KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT

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

class GetPath(nps.BoxTitle):
	_contained_widget = nps.Textfield

class OpenForm(nps.FormBaseNew):
	def create(self):
		y,x = self.useable_space()
		self.box1 = self.add(
			RecentlyOpened, name="recently opened files",
			relx=0, rely=0, 
			max_width=x//2-1, max_height=y-5
		)
		self.box1.create()
		self.box2 = self.add(
			NamesPaths, name="saved paths",
			relx=x//2-1, rely=0,
			max_width=x//2-1, max_height=y-5
		)
		self.box2.create()
		self.box3 = self.add(
			GetPath, name="input path",
			relx=1, rely=-5,
			max_width=x-3, max_height=3
		)
		self.add_event_hander("READINGEVENT", self.cgpath)
	def while_waiting(self):
		self.parentApp.queue_event(nps.Event("READINGEVENT"))
	def cgpath(self,e):
		pass
