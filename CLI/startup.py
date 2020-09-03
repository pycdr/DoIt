import	prompt_toolkit as ptk
from	prompt_toolkit import HTML, print_formatted_text as print
from	prompt_toolkit.styles import Style
import	click
import	json

style = Style.from_dict(json.loads(open("./style.json"),'r'))
@click.group
def opening():
	pass
@opening.command
def welcome():
	print(HTML("<welcome_message>\
	welcome to the DoIt program!\
	</welcome_message>"),style=style)

def recently_opened_show(ctx, param, value):
	if not value or ctx.resilient_parsing:
		return
	temp = open("./recently_opened",'r').read()
	l = [x.split(",") for x in temp.split("\n")]
	# coming soon...!
	clicl.exit()
@click.option("--recently",is_eager=True,callback=recently_opened_show)
