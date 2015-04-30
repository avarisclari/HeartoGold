//#!/usr/bin/env rdmd

import std.stdio;
import core.stdc.stdlib;
import std.process;
import core.thread;
import std.string;

void main()
{
	write("" , "\n");//Title Text area
	write("1 New Game" , "\n" , "2 About" , "\n");
	write("0 Quit", "\n");
	write("Your Choice: ");
	int UserInput; //Calls for User Input (self explanatory really)
	readf("%s", &UserInput);//Reads it
	if(UserInput == 1){ 
		goto opening; //Example Label (will work on reading from seperate text file soon
	}
	if(UserInput == 2){
		goto about;
	}
	if(UserInput ==	0){
		abort();//Current quit mechanism
	}
opening: {
	write("Blah.");
	write("\n\n", "1 No.", "\n", "2 No.", "\n", "0 Quit", "\n");
	write("Your Choice: ");
	int UserInput2;
	readf("%s", &UserInput2); //Numeric Variables Until I figure out how to declare properly
	if(UserInput2 == 1){
		abort();
		}
	if(UserInput2 == 2){
		abort();
		}
	if(UserInput2 == 0){
		abort();
	}
}
about:
{
	write("Nothing.");
	write("1 Quit");
	int UserInput88;
	readf("%s", &UserInput88);
	if(UserInput88 == 0){
		abort();
		}
}
}
