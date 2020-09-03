from convert import PDict
from exporter import dict_to_pickle
from pprint import pprint
prg = PDict("example program","this is an example")
for x in range(1,31):
	prg.set_day(x,title="day"+str(x))
prg.set_time(1,"10:00","24:00","mylife!")
pprint(prg.output)
dict_to_pickle(prg.output,"./test.pckl")
print("done!")
