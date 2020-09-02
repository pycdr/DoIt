class PDict:
	def __init__(self,
	name,bio="",
	program_type="month30",length=30,
	start_from=("sun",1)):
		self.output = {
			"name":name,
			"bio":bio,
			"Ptype":program_type,
			"length":length,
			"Dfrom":start_from,
			"days":[]
		}
	@property
	def name(self):
		return self.output["name"]
	@name.setter
	def name(self,value):
		self.output["name"] = value
	@property
	def bio(self):
		return self.output["bio"]
	@bio.setter
	def bio(self,value):
		self.output["bio"] = value
	@property
	def program_type(self):
		return self.output["Ptype"]
	@program_type.setter
	def program_type(self,value):
		self.output["Ptype"] = value
	@property
	def length(self):
		return self.output["length"]
	@length.setter
	def length(self,value):
		self.output["length"] = value
	@property
	def start_from(self):
		return self.output["Dfrom"]
	@start_from.setter
	def start_from(self,value):
		self.output["Dfrom"] = value
	def set_day(self,number,**args):
		if number<=len(self.output["days"]):
			for arg in args:
				self.output["days"][number-1][arg]=args[arg]
			self.output["days"][number-1]["hours"]=[]
		elif number==len(self.output["days"])+1:
			self.output["days"].append({
				"title":args.get("title",""),
				"color":args.get("color",""),
				"icon":args.get("icon",""),
				"hours":[]
			})
		else:
			for x in range(len(self.output["days"])-number-1):
				self.output["days"].append({
					"title":"",
					"color":"",
					"icon":"",
					"hours":[]
				})
			self.set_day(number,**args)
	def set_time(self,day_number,time_start,time_end,title="",color="",icon=""):
		time_start = [int(x) for x in time_start.split(":")]
		time_end = [int(x) for x in time_end.split(":")]
		ts = time_start[0]*60+time_start[1]
		te = time_end[0]*60+time_end[1]
		if time_start == time_end:
			raise Exception("in this version, time should be like a range, not just a time.")
		elif ts>te:
			raise ValueError("end time should be larger than start time")
		else:
			chng = False
			n = 0
			for x in self.output["days"][day_number-1]["hours"]:
				ts2 = x["time"][0][0]*60+x["time"][0][1]
				te2 = x["time"][1][0]*60+x["time"][1][1]
				if ts<ts2<te or ts<te2<te:
					raise Exception("in this version, times can't have any joint part.")
				elif te<ts2:
					break
				elif ts==ts2 and te==te2:
					chng = True
				n+=1
			if chng:
				self.output["days"][day_number-1]["hours"]["title"]=title
				self.output["days"][day_number-1]["hours"]["color"]=color
				self.output["days"][day_number-1]["hours"]["icon"]=icon
			self.output["days"][day_number-1]["hours"].insert(n,{
				"title":"",
				"color":"",
				"icon":"",
				"time":[time_start, time_end]
			})
			return True
