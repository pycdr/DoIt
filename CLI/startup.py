import npyscreen as nps
from Objects.OpenObjects import OpenForm

class App(nps.StandardApp): #or: nps.NPSAppManaged
	def onStart(self):
		self.openform = self.addForm("MAIN", OpenForm)
		self.daysform = None
		self.dayform =  None
		self.timeform = None
		
if __name__=="__main__":
	try:
		App().run()
	except KeyboardInterrupt:
		print("Exit by pressing ^C")
