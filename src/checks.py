import os
import sys

global command_list

command_list = ["sip", "srch", "help"]

#check if cowsay is installed
def check_cowsay():
    pass


#check if lolcat is installed
def check_lolcat():
    pass


#checks if figlet is installed
def check_figlet():
    pass


#checks if inputed command is in command_list
def check_command(cmd_str):

    #checks if command is help so its not spotted as wrong
    if cmd_str[0] == "help":
        #returns True because it does not have a parameter
        return True

    #checks list and parameter
    elif cmd_str[0] in command_list and cmd_str[1] != "" or None:
        #returns True if command in list
        return True

    else:
        #returns False if command not in list
        return False


def check_command_sec(cmd_str):


    #checks list
    if cmd_str != "" or None:
        #returns True if command is not empty
        return True

    else:
        #returns False if command is empty or None
        return False
