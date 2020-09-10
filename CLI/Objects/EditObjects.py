import npyscreen as nps
import os
import sys
sys.path.append("../exporter")
import convert, to_pickle as tpk

wdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']

class DaysForm(nps.ActionForm):
	def create(self):
		y,x = self.useable_space()
		if not hasattr(self,"data") or hasattr(self,"wdate"):
			return
		self.wtitle = self.add(
			nps.FixedText, max_height=3,
			value = self.data["name"]+" | "+self.data["bio"]
		)
		table_data = [[]]
		for x in range(wdays.index(self.data["Dfrom"][0])):
			table_data[0].append("<--->")
		n=self.data["Dfrom"][1]
		for x in range(self.data["length"]):
			if len(table_data[-1])==7:
				table_data.append([])
			table_data[-1].append(str(n)+" | "+self.data["days"][0]["title"])
			n+=1
		self.wdate = self.add(
			nps.GridColTitles, name=self.data["name"],
			#column_width=x//7-3, row_height=y//2-4,    ---> amazing BUG!
			col_titles=["sun","mon","tue","wed","thu","fri","sat"],
			values=table_data
		)
	def submit_path(self,path):
		if not os.path.exists(path):
			nps.notify_wait("Please give an exists path!")
			exit(0)
		self.path = path
		self.data = tpk.pickle_to_dict(self.path)
		self.create()
	def on_cancel(self):
		self.parentApp.setNextForm("MAIN")
