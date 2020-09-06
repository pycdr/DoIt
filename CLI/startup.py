import npyscreen as nps
from Objects.OpenObjects import OpenForm

class App(nps.NPSAppManaged):
	def onStart(self):
		self.registerForm("MAIN", OpenForm())

if __name__=="__main__":
	App().run()
