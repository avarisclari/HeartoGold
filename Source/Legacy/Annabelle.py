#!python
# Annabelle.py
# An Interactive Fiction engine by Christopher "avarisclari" Weigle

import textwrap
import sys
import string
import os

sys.stdout.write("\x1b]2;Annabelle\x07")

scenes = {
    "title": {
        "description": "You can put a title graphic here in Ascii format or just plain text",
        "paths": [
            { "go_to": "opening", "phrase": "Start a New Game" },
            { "go_to": "about", "phrase": "About" }
            ]
        },
    "opening": {
        "description": "Enter a description for the opening scene here.",
        "paths": [
            { "go_to": "optiona", "phrase": "Goes to scene labeled optiona." },
            { "go_to": "optionb", "phrase": "Goes to scene labeled optionb." },
            ]
},
    "about": {
        "description": "This engine is currently a prototype. I'm working on "
                       "making a full engine. Please enjoy it.\n\n Christopher "
                       "avarisclari\" Weigle",
        "paths": [
            { "go_to": "title", "phrase": "Return to Title" }
            ]
        }
}

scene = scenes["title"]

while 1 == 1:
    next_choice = None
    paths = scene["paths"]
    description = scene["description"]
    lines = string.split("\n")

    for line in lines:
        if len(line > 55):
            w = textwrap.TextWrapper(width=45, break_long_words=False)
            line = '\n'.join(w.wrap(line))
        decription += line +"\n"
    print description



    #Shows the choices
    for i in range(0, len(paths)):
        path = paths[i]
        menu_item = i + 1
        print "\t", menu_item, path["phrase"]

    print "\t(0 Quit)"

    #Get user selection

    prompt = "Make a selection ( 0 - %i): \n" % len(paths)

    while next_choice == None:
        try:
            choice = raw_input(prompt)
            menu_selection = int(choice)

            if menu_selection == 0:
                next_choice = "quit"
            else:
                index = menu_selection - 1
                next_choice = paths[ index ]

        except(IndexError, ValueError):
                print choice, "is not a valid selection"

    if next_choice == "quit":
        print "Thanks for playing."
        sys.exit()
    else:
        scene = scenes[ next_choice["go_to"] ]
        print "You decided to:", next_choice["phrase"], "\n"
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")
