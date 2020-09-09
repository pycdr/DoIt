import npyscreen as nps
from Objects.OpenObjects import OpenForm, RecentlyOpened, NamesPaths, GetPath

class App(nps.StandardApp): #or: nps.NPSAppManaged
	def onStart(self):
		self.openform = self.addForm("MAIN", OpenForm)
		self.openformb1 = self.addForm("OPENFORM1", RecentlyOpened)
		self.openformb2 = self.addForm("OPENFORM2", NamesPaths)
		self.openformb3 = self.addForm("OPENFORM3", GetPath)
		self.daysform = None
		self.dayform =  None
		self.timeform = None
		
if __name__=="__main__":
	try:
		App().run()
	except KeyboardInterrupt:
		print("Exit by pressing ^C")
