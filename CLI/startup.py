import	prompt_toolkit as ptk
from	prompt_toolkit import HTML, print_formatted_text as print
from	prompt_toolkit.styles import Style
import	json
import	argparse
import	os

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
args = parser.parse_args()
if args.recently:
	show_recently_opened()
	exit()
parser.add_argument("path", metavar="path", type=str, help="to load data from pickle file.")
args = parser.parse_args()

print(HTML("<welcome_message>\
welcome to the DoIt program!\
</welcome_message>"),style=style)
