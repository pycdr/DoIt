import npyscreen as nps
import os

class OpenForm(nps.Form): #or: nps.Form
	def create(self):
		y, x = self.useable_space()
		self.form1 = self.add(
			RecentlyOpenedForm,
			relx=0,
			rely=0,
			max_width=x//2-2,
			max_height=(3*y)//4,
			name="recently openeds"
		)
		self.form2 = self.add(
			OpenByNameForm,
			relx=x//2,
			rely=0,
			max_width=x//2-2,
			max_height=(3*y)//4,
			name="defined names"
		)
		self.form3 = self.add(
			OpenByPathForm,
			relx=0,
			rely=(3*y)//4,
			max_width=x-2,
			max_height=y//4,
			name = "input path"
		)
	def afterEditing(self):
		self.parentApp.setNextForm(None)

class RecentlyOpenedWidget(nps.TitleSelectOne):
	value=[1,]
	name="openeds"
	values = [
		"["+x.split(",")[1]+"]: "+x.split(",")[0] 
		for x in open("recently_opened",'r').read().split("\n") 
		if(not x=="")and(not x.isspace())
	]
	scroll_exit=True
	#self._contained_widget = self.add(self.TitleSelectOne,)

class RecentlyOpenedForm(nps.BoxTitle):
	_contained_widget = RecentlyOpenedWidget

class OpenByPathForm(nps.BoxTitle):
	def create(self):
		self.add(nps.OptionFreeText, name="path: ")
	def afterEditing(self):
		pass

class OpenByNameForm(nps.BoxTitle):
	def create(self):
		pass
	def afterEditing(self):
		pass
