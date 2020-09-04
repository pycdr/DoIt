_weekdays = ["sun","mon","tue","wed","thu","fri","sat"]

def output(data):
	if data["Ptype"]=="week":
		output_7(data)
	elif data["Ptype"]=="month31":
		output_31(data)
	elif data["Ptype"]=="month30":
		output_30(data)
	elif data["Ptype"]=="month29":
		output_29(data)
	else:
		if data["length"] in {7,29,30,31}:
			{
				7:output_7,
				31:output_31,
				30:output_30,
				29:output_29
			}[data["length"]](data)
		else:
			output_N(data)

def output_7(data):
	pass

def output_31(data):
	pass
	
def output_30(data):
	pass
	
def output_29(data):
	pass
	
def output_N(data):
	pass
