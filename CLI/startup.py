import	prompt_toolkit as ptk
from	prompt_toolkit		import HTML, print_formatted_text as print
from	prompt_toolkit.styles	import Style
from	output_data		import output
import	json
import	argparse
import	os, sys

sys.path.append("../")
import	exporter

style = Style.from_dict(json.loads(open("./style.json",'r').read()))

def show_recently_opened():
	s = open("./recently_opened",'r').read()
	for x in s.split("\n"):
		if x=="" or x=="," or x.isspace():
			continue
		l = x.split(",")
		print(HTML("<time>["+l[1]+"]</time> ~> "+l[0]),style=style)

parser = argparse.ArgumentParser(description="an app to schedule your life or your work.")
parser.add_argument("--recently", required=False, action="store_true", help="get recently opened pickles.")
parser.add_argument("-l", "--list", required=False, action="store_true", help="show list of names for schedule")
parser.add_argument("--path", required=False, metavar="path", type=str, help="to load data from pickle file(it can be a name).")
args = parser.parse_args()

if args.recently:
	show_recently_opened()
	exit()
if args.list:
	d = json.loads(open("./set_path.json", 'r').read())
	if len(d)==0:
		print(HTML("<info>oops! there is not any name in list!</info>"),style=style)
	for x in d:
		print(HTML("<schname>["+x+"]</schname>: "+d[x]),style=style)
	exit()
	
print(HTML("<welcome_message>\
welcome to the DoIt program!\
</welcome_message>"),style=style)
path = ""
if args.path:
	if os.path.isfile(args.path):
		print("you set path as "+args.path)
		path = args.path
		if not args.path.endswith(".pckl"):
			print(HTML(
"<warn>the given path doesn't seem a pickle file\n\
if you're not sure that it's pickle, we will get an error!\n\
we suggest you to save our data as pickle(.pckl) file, thanks!</warn>"),style=style)
	else:
		d = json.loads(open("./set_path.json", 'r').read())
		if args.path in d:
			print("you set path as "+d[args.path])
			path = d[args.path]
			if not d[args.path].endswith(".pckl"):
				print(HTML(
"<warn>the given path doesn't seem a pickle file\n\
if you're not sure that it's pickle, we will get an error!\n\
we suggest you to save our data as pickle(.pckl) file, thanks!</warn>"),style=style)
		else:
			print(HTML("<error>please give an existing pickle file path or saved name!</error>"),style=style)
			exit()

dt = exporter.pickle_to_dict(path)
data = exporter.PDict("")
data.output = dt

output(data)
