import npyscreen as nps
import os
import json
import curses
from curses import KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT

_l1 = [
	x
	for x in open("recently_opened",'r').read().split("\n")
	if(not x=="")and(not x.isspace())
]
rclist = [
	"["+x.split(",")[1]+"]: "+x.split(",")[0]
	for x in _l1
]
name_dict = json.load(open("set_path.json",'r'))

class RecentlyOpened(nps.ActionForm):
	def create(self):
		self.wmain = self.add(
			nps.TitleSelectOne, name="choose one of the files", value=[],
			values=rclist, scroll_exit=True
		)
	def on_ok(self):
		path = _l1[self.wmain.value[0]].split(",")[0]
		self.parentApp.daysform.submit_path(path)
		self.parentApp.setNextForm("EDITFORM1")
	def on_cancel(self):
		self.parentApp.setNextForm("MAIN")

class NamesPaths(nps.ActionForm):
	def create(self):
		self.wmain = self.add(
			nps.TitleSelectOne, name="choose one of the files", value=[],
			values=[x+" : "+name_dict[x] for x in name_dict], scroll_exit=True
		)
	def on_ok(self):
		path = name_dict[list(name_dict.keys())[self.wmain.value[0]]]
		self.parentApp.daysform.submit_path(path)
		self.parentApp.setNextForm("EDITFORM1")
	def on_cancel(self):
		self.parentApp.setNextForm("MAIN")

class GetPath(nps.ActionForm):
	def create(self):
		self.wmain = self.add(nps.Textfield, name="input path") 
	def on_ok(self):
		path = self.wmain.value
		self.parentApp.daysform.submit_path(path)
		self.parentApp.setNextForm("EDITFORM1")
	def on_cancel(self):
		self.parentApp.setNextForm("MAIN")

class OpenForm(nps.ActionForm):
	def create(self):
		y,x = self.useable_space()
		self.selecting = self.add(
			nps.TitleSelectOne, max_height=y-4, value=[],
			name="how to get path?", values=["show recently opened files", "Select by saved paths", "input path"], 
			scroll_exit=True
		)
	def on_ok(self):
		if len(self.selecting.value)==0:
			nps.notify_wait("first, Please select one of the choices!")
			return
		self.parentApp.setNextForm(
			{
				"show recently opened files": "OPENFORM1",
				"Select by saved paths": "OPENFORM2",
				"input path": "OPENFORM3"
			}[self.selecting.values[
				self.selecting.value[0]
			]]
		)
	def on_cancel(self):
		if nps.notify_yes_no("Do you want to exit", title="Exit",editw=1):
			nps.notify_wait("Bye..!")
			exit()
