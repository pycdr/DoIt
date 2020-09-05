import npyscreen as nps

class App(nps.NPSApp):
	def main(self):
		self.forms = [
			nps.Form(name="open file"),
			nps.Form(name="edit days"),
			nps.Form(name="edit hours"),
			nps.Form(name="edit hour")
		]
		# ...
		self.forms[0].edit()

if __name__=="__main__":
	App().run()
