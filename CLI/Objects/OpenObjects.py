import npyscreen as nps
import os

width, height = os.get_terminal_size()

class OpenForm(nps.ActionForm):
	def create(self):
		y, x = self.useable_space()
		self.form1 = self.add(
			OpenByPathForm,
			relx=0,
			rely=0,
			max_width=x//2-2,
			max_height=y//2-2,
			name="recently openeds"
		)
		self.form2 = self.add(
			OpenByNameForm,
			relx=x//2+1,
			rely=0,
			max_width=x//2-2,
			max_height=y//2-2,
			name="defined names"
		)
		self.form3 = self.add(
			OpenByPathForm,
			relx=0,
			rely=y//2+1,
			max_width=x-2,
			max_height=(3*y)//4,
			name = "input path"
		)
	def afterEditing(self):
		self.parentApp.setNextForm(None)

class RecentlyOpenedForm(nps.BoxTitle):
	def create(self):
		if not hasattr(self,"rclist"):
			self.rclist = [x.split(":") for x in open("../recently_opened",'r').read().split("\n")]
		for x in self.rclist:
			self.add(
				nps.SelectOne,
				name="["+x[1]+"]: "+x[0]
			)

class OpenByPathForm(nps.BoxTitle):
	def create(self):
		self.add(nps.Filename, name="path: ")
	def afterEditing(self):
		pass

class OpenByNameForm(nps.BoxTitle):
	def create(self):
		self.add(nps.Filename, name="path: ")
	def afterEditing(self):
		pass
