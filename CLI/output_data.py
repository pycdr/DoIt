from CLITable import output_table

_weekdays = ["sun","mon","tue","wed","thu","fri","sat"]

def output(data):
	print("type:",data.program_type)
	if data.program_type=="week":
		output_7(data)
	elif data.program_type=="month31":
		output_31(data)
	elif data.program_type=="month30":
		output_30(data)
	elif data.program_type=="month29":
		output_29(data)
	else:
		if data.output["length"] in {7,29,30,31}:
			{
				7:output_7,
				31:output_31,
				30:output_30,
				29:output_29
			}[data["length"]](data)
		else:
			output_N(data)

def output_7(data):
	if data.start_from[0]==_weekdays[0]:
		l = [[str(x["title"]) for x in data.output["days"]]]
		output_table(l,start_from=data.start_from[1],start_weekday_from=data.start_from[0])
	else:
		l = [
			[str(x["title"]) for x in data.output["days"][0:8-data.start_from[1]]],
			[str(x["title"]) for x in data.output["days"][8-data.start_from[1]::]]
		]
		output_table(l,start_from=data.start_from[1],start_weekday_from=data.start_from[0])
def output_31(data):
	pass
	
def output_30(data):
	pass
	
def output_29(data):
	pass
	
def output_N(data):
	pass
