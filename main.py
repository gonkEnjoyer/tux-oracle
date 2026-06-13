import random
import cowsay
from rich.console import Console

console = Console()

options = [
	"yes", 
	"no", 
	"maybe", 
	"ask again later", 
	"it is unclear", 
	"I cannot foresee", 
	"signs point to yes", 
	"affirmative", 
	"nein", 
	"it appears not"
]

silent_options = [
	"speak up, child",
	"you remain silent...",
	"I await your question",
	"tux knows all (or at least most) things"
]

running = True

while running:
	query = console.input("[underline]What is the wisdom you seek[blink]?[/][/] ")
	
	if len(query) == 0:
		response = random.choice(silent_options)
	else:
		response = random.choice(options)	

	text = cowsay.get_output_string("tux", response)

	styled_text = text.replace(response, f"[bold yellow]{response}[/]")

	console.print(styled_text, highlight = False)

	if console.input("Press [blue italic]<enter>[/] to consult [bold yellow]tux the oracle[/] or [blue italic]q[/] to quit: ") == "q":
		running = False	
