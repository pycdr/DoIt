from argparse import ArgumentParser as AP
from rich.console import Console
from rich.table import Table
import sys
sys.path.append("../exporter")
import convert, to_pickle as tpk


parser = AP(description="DoIt: live and organize!")
console = Console()

parser.add_argument(
	"path",metavar="path/to/file.pckl",type=str,
	help="path of pickle file"
)
parser.add_argument(
	"--day",type=int,required=False,
	help="number of day to show"
)
parser.add_argument(
	"--time",type=str,required=False,
	help="time of day to show(not completed)"
)

args = parser.parse_args()
data = tpk.pickle_to_dict(args.path)
def hour(l):
	out = ""
	t1,t2 = int(l[0]),int(l[1])
	f = lambda x: "0"+str(x) if x<10 else str(x)
	return f(t1)+":"+f(t2)
if not args.day:
	console.print(data["name"]+" | "+data["bio"])
	table = Table(show_header=True)
	wdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
	for x in wdays:
		table.add_column(x,justify='center')
	table_data=[[]]
	for x in range(wdays.index(data["Dfrom"][0])):
		table_data[0].append("<--->")
	n=data["Dfrom"][1]
	for x in range(data["length"]):
		if len(table_data[-1])==7:
			table_data.append([])
		color = data["days"][x]["color"]
		if not color:
			color="white"
		table_data[-1].append(
			"["+color+"]"+
			str(n)+" | "+data["days"][x]["title"]+
			"[/"+color+"]")
		n+=1
	for x in table_data:
		table.add_row(*x)
	console.print(table)
	exit()
elif not args.time:
	dn = args.day
	day = data["days"][dn-data["Dfrom"][1]]
	color = data["days"][dn-data["Dfrom"][1]]["color"]
	if not color:
		color="white"
	console.print("["+color+"]"+day["title"]+"[/"+color+"]")
	for x in day["hours"]:
		c = x["color"]
		if not c:
			c="white"
		console.print(
			"~> ["+color+"]"+
			"from "+hour(x["time"][0])+" to "+hour(x["time"][1])+"["+color+"]")
		if x["title"]:
			console.print("title: "+x["title"])
		else:
			console.print("nothing to show")
