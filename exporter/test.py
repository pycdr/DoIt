from convert import PDict
from to_pickle import dict_to_pickle
from pprint import pprint
"""
prg = PDict("example program","this is an example")
for x in range(1,31):
	prg.set_day(x,title="day"+str(x))
prg.set_time(1,"10:00","24:00","mylife!")
pprint(prg.output)
dict_to_pickle(prg.output,"./test.pckl")
print("done!")
"""
prg = PDict("example program","this is an example")#,program_type="week",length=7)
prg.program_type = "week"
prg.length = 7
#prg.output["program_type"] = "week"
#prg.output["length"] = 7
for x in range(1,8):
	prg.set_day(x,title=("day"+str(x) if x%3== else ""))
prg.set_time(1,"10:00","24:00","mylife!")
pprint(prg.output)
dict_to_pickle(prg.output,"./test.pckl")
print("done!")
