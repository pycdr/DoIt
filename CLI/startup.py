import npyscreen as nps
from Objects.OpenObjects import OpenForm

class App(nps.StandardApp): #or: nps.NPSAppManaged
	def onStart(self):
		self.addForm("MAIN", OpenForm, name="open")
		
if __name__=="__main__":
	try:
		App().run()
	except KeyboardInterrupt:
		print("Exit by pressing ^C")
