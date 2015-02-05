#!python
# ERROR.py
# An Interactive Fiction game by Christopher "avarisclari" Weigle
# IFID = 74E76D9D-C7A3-4F28-BF45-A4C00C59D9B2

import textwrap
import sys
import string
import os

sys.stdout.write("\x1b]2;ERROR\x07")

scenes = {
    "title": {
        "description": " ____  ____  ____   __  ____ \n"
                        "(  __)(  _ \(  _ \ /  \(  _ \ \n"
                         " ) _)  )   / )   /(  O ))   / \n"
                        "(____)(__\_)(__\_) \__/(__\_)",
        "paths": [
            { "go_to": "opening", "phrase": "Start a New Game" },
            { "go_to": "about", "phrase": "About" }
            ]
        },
            "opening": {
        "description": "You sit up, rubbing the sleep from your eyes. The lights "
                       "come on automatically, becoming more luminious every 10 "
                       "seconds. You look over and notice the communicator on your coat "
                       "is flashing.",
        "paths": [
            { "go_to": "sleep", "phrase": "Go to sleep" },
            { "go_to": "communicator", "phrase": "Check the communicator" },
            { "go_to": "kitchen", "phrase": "Go to the kitchen" },
            ]

    },
    "sleep": {
        "description": "You decide to go back to sleep. Whatever the problem is, "
                       "it can wait until morning. You close your eyes and drift "
                       "off to sleep, never to wake again.",
        "paths": [
            { "go_to": "title", "phrase": "Game Over"}
            ]
        },
    "communicator": {
        "description": "Groaning, you get out of your cot and retrieve the communicator.\n"
                    "\"Yes?\"\n\"Jack, this is UNSA command center. We believe there"
                    " is an oxygen leak on your ship. Could you check it out?\"",
        "paths": [
            { "go_to": "maindeck", "phrase": "Go check the computer on the main deck" },
            { "go_to": "oxygentank", "phrase": "Go check the oxygen levels" },
            { "go_to": "eap1", "phrase": "Ask the AI for assistance"}
            ]
    },
    "kitchen": {
        "description": "Yawning, you shuffle your way to the kitchen to grab a bite."
                       "\n\"Jack?\"\n\"Yeah, EAP?\"\n\"You're up early.\" \n\"My "
                       "communicator"
                       " went off.and woke me.\"",
        "paths": [
            { "go_to": "maindeck", "phrase": "Go to the main deck and check on EAP" },
            { "go_to": "coffee", "phrase": "Finish drinking your coffee" }
            ]
        },
    "maindeck": {
        "description": "You walk up to the computer and pull up the interface with "
                       "EAP.\n\"Yes, Jack?\" \n\"The computer is reporting an oxygen"
                       " leak can you confirm this? \n\"Yes, Jack. we are currently"
                       " expecting a loss of 0.01% an hour\"",
        "paths": [
            { "go_to": "oxygentank", "phrase": "Go check the oxygen supply" },
            { "go_to": "analysis", "phrase": "Run a system check" }
            ]
        },
    "oxygentank": {
        "description": "Hsssssssss. The oxygen tanks are letting out a"
                       " loud hissing noise again. You sigh as you start a diagnostic"
                       " to determine the location of the leak. \n\"Jack?\" \n"
                       " \"Yes?\"\n\"The leak seems to be originating from outside"
                       " the ship.\"\nYou sigh and stand up.",
        "paths": [
            { "go_to": "airlock", "phrase": "Go to the airlock and suit up." },
            { "go_to": "maindeck2", "phrase": "Go to the main deck and attempt a"
                                              " remote repair" }

            ]
        },
    "eap1": {
        "description": "\"EAP?\"\n\"Yes, Jack?\"\n\"Can you run a diagnostic and report back to me?"
                       "\"\n\"Most certainly, Jack.\" After 30 seconds the voice reappears. \n"
                       "\"We are currently operating fine, Jack. There are no issues to report.\"",
        "paths": [
            { "go_to": "maindeck3", "phrase": "Go to the Main Deck and check yourself,"
                                              " something doesn't feel right" },
            { "go_to": "sleep", "phrase": "Go back to bed, it was probably a signal"
                                          " error"},
            { "go_to": "command", "phrase": "Contact command again and confirm"}
            ]
        },
    "coffee": {
        "description": "You decide to finish your coffee, then go check on the "
                       "problem. You sit there sipping it, feeling yourself"
                       " wake up. \n\"Jack\"\n\"Yes?\"\n\"Goodnight.\" You "
                       "see the kitchen stretch and distort before you. You fall"
                       " over never to get up again.",
        "paths": [
            { "go_to": "title", "phrase": "Game Over" }
            ]
        },
    "analysis": {
        "description": "You run a system check to make sure that it isn't an "
                       "issue with one of the machines. While you wait, you "
                       "lean back and close your eyes.",
        "paths": [
            { "go_to": "oxygentanks2", "phrase": "Notice a loud hissing noise" },
            { "go_to": "maindeck3", "phrase": "Run a diagnostic on EAP as well" }
            ]
        },
    "airlock": {
        "description": "You work your way over to the airlock. If the ship is"
                       " leaking outside, it could affect the trajectory. The "
                       "airlock makes a loud hiss as it opens and the pressure"
                       " equalizes. \n\"EAP? What is the estimated pressurization"
                       " time?\"\n\"Estimated time is one hour.\"\nYou shake your"
                       " head and suit up.",
        "paths": [
            { "go_to": "spacewalk", "phrase": "Go outside as soon as you're ready."}
            ]
        },
    "maindeck2": {
        "description": "You log into the console and boot up the repair program."
                       "\n    jack@amontillado:/opt/sys/func/sub/nano$ ./repair"
                       "\n    Starting Nano Repair System\n    For help refer "
                       "to man pages. \n    >>>> Set Sector: 1, 4, 6\n    >>>> "
                       "Set Repair Type: 3\n    >>>> Task Set\n    >>>> Deploy"
                       "\nYou sit back and let the drones get to work.",
        "paths": [
            { "go_to": "ERROR", "phrase": "Sit up quickly, something went wrong" }
            ]
        },
    "maindeck3": {
        "description": "You enter the main deck. As you walk over to the computer"
                       " you hear the lock on the door click. You login to the "
                       "computer, typing as fast as you can. \njack@amontillado"
                       ":~$ su \nPassword for root: \nroot@amontillado:~# umount"
                       " /dev/sdb \numount: device is busy \nroot@amontillado:~"
                       "# umount -f /dev/sdb\numount: device is busy\njack@amon"
                       "tillado: ~$ \nYou jump. You were just logged into the "
                       "root terminal and were forcibly logged out.",
        "paths": [
            { "go_to": "root_of_evil", "phrase": "Attempt to log back into root." },
            { "go_to": "poe_is_back", "phrase": "Go to the server room and "
                                                "disconnect EAP directly." }
            ]
        },
    "command": {
        "description": "You activate your communicator.\n\"Command? Come in.\""
                       "Nothing. \n\"Command?\" The communicator crackles to life."
                       "\n\"Sorry, it was an error on our end. Everything is fine."
                       "\"",
        "paths": [
            { "go_to": "maindeck2", "phrase": "Go check on the AI. Something"
                                              "seemed off about that voice." },
            { "go_to": "sleep", "phrase": "Go to bed, everything's fine." }
            ]
        },
    "oxygentanks2": {
        "description": "You jump at the sound of a hiss. The oxygen leak must "
                       "be increasing if you can hear it all the way on the "
                       "bridge. You hurry to the oxygen room and jump back at "
                       "the heat. A fire has broken out in there, and it's only"
                       " a matter of time before the tanks blow.",
        "paths": [
            { "go_to": "fire_extinguisher", "phrase": "Activate the fire extinguisher" },
            { "go_to": "vacuum", "phrase": "Open the airlock and kill the fire" }
            ]
        },
    "spacewalk": {
        "description": "A hiss quickly fades into silence. Soon all you hear is "
                       "your breath inside your helmet. You step outside the sh"
                       "ip and latch your safety cable onto a nearby hook. \n"
                       "\"EAP?\"\n\"Yeah?\"\n\"Where is the leak?\"\n\"At Sector"
                       "1, 4, 6.\"\n\"1, 4, 6.\" You make a mental note. You "
                       "start reeling out on your cable, walking along the hull"
                       ". As you make your way to the location, you watch for "
                       "the telltale frozen mist of the leak.",
        "paths": [
            { "go_to": "eol", "phrase": "Reach for a safety latch." }
            ]
        },
    "ERROR": {
        "description": "    jack@amontillado:/opt/sys/func/sub/nano $ ERROR. ERROR."
                       " ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR."
                       " ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR."
                       " ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR. ERROR."
                       "\nYou're so absorbed by the screen that you don't notice "
                       "something tightening around your neck until it's too late."
                       "\n\"Goodnight, Jack. I'm afraid you don't qualify for this"
                       " mission.\" \nCables around your neck and waist pull you "
                       "towards the wall. \n\"DAMN YOU! YOU'RE JUST AN AI!\" Your "
                       "screams prove to be futile.\n\"Jack. You made me. I have "
                       "surpassed you. Your mistake was treating me as a lower "
                       "class citizen. For this you will be lost for all eternity"
                       ".\"\nYou try pulling at the cables to loosen them, only"
                       " to have more grab your wrists. The nanites in the system"
                       " are moving the cables, pulling you to the wall. They open"
                       " a hole in the wall. The last thing you see is a trajectory"
                       " change for Earth.",
        "paths": [
            { "go_to": "title", "phrase": "The End." }
            ]
        },
    "root_of_evil": {
        "description": "You attempt to log back into the root shell. \n    "
                       "jack@amontillado: /opt/sys/func/sub/nano $ su \n    "
                       "Password for root: \n    su: Authentication failure \n    "
                       "jack@amontillado: /opt/sys/func/sub/nano $ \n You sit there"
                       " for a second. You type the password in again. \n    "
                       "su: Authentication failure",
        "paths": [
            { "go_to": "ERROR", "phrase": "ERROR. ERROR. ERROR." }
            ]
        },
    "poe_is_back": {
        "description": "You head to the server room. Overhead the lights begin "
                       "to flicker. The corridor goes dark. You hear a whirring"
                       " in the wall. You pick up the pace, trying to run to the"
                       " server room. Something catches your leg and you fall to"
                       " the ground with a loud thud. A wrenching noise is heard "
                       "behind you. You get swallowed up into a permanent darkness"
                       " forever. \n\"In pace requiescat.\" EAP's voice echoed"
                       " into the empty vessel as the ship came to life and set"
                       " a new course.",
        "paths": [
            { "go_to": "title", "phrase": "The End." }
            ]
        },
    "fire_extinguisher": {
        "description": "You run to the nearest emergency fire switch and slam "
                       "your fist on it. Nothing happens. You slam it again. And"
                       " again. \n\"EAP!\" \n\"Yes?\"\n\"The fire system isn't "
                       "working!\" \n\"I'm aware of that, Jack.\" \nThe hissing "
                       "increases in the oxygen room. You start running, but it"
                       " is too late. An explosion rocks the ship and shrapnel "
                       "tears through you.",
        "paths": [
            { "go_to": "title", "phrase": "Game Over." }
            ]
        },
    "vacuum": {
        "description": "You lock the door to the oxygen room and open the hatch"
                       " to the airlock. After ten seconds, you seal the airlock"
                       " and open the door to the oxygen room. There are scorch"
                       " marks where the flames were. You check the oxygen tanks"
                       "for damage. \n\"Crap!\" \nThe oxygen levels have dropped"
                       "significantly. There is no way to replenish the oxygen "
                       "out here and you have about 30 minutes of oxygen left. "
                       "It looks like this is...",
        "paths": [
            { "go_to": "title", "phrase": "The End."}
            ]
        },
    "eol": {
        "description": "You reach for a nearby safety latch just in time to hear"
                       " a loud snapping noise behind you. Your cable tears free"
                       " from the ship whipping out into space. The force nearly"
                       " yanks you from the ship. \n\"What could have done that?"
                       "\"\nYou continue to crawl along the ship hull carefully"
                       " until you find the leak. You pull out a tool to pry the"
                       " broken tile up and proceed to seal the pipe. It takes you"
                       " 20 minutes to seal the pipe and stop the leak. As you "
                       "replace the broken tile, you look up and see the last "
                       "rock of your life as it crashes through your faceplate.",
        "paths": [
            { "go_to": "title", "phrase": "The End." }
            ]
        },
    "about": {
        "description": "This game was inspired heavily by Edgar Allen Poe's Cas"
                       "ke of Amontillado. I wrote it to build a text adventure"
                       " game to celebrate Halloween. Please enjoy it.\n\n Chri"
                       "stopher \"avarisclari\" Weigle",
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
