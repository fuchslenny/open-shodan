import os
import sys

global command_list

command_list = ["sip", "help"]

#check if cowsay is installed
def check_cowsay():
    pass


#check if lolcat is installed
def check_lolcat():
    pass


#checks the choice choosen in the menu
def check_menu_choice():
    pass


#checks if inputed command is in command_list
def check_command(cmd_str):

    #checks list
    if cmd_str in command_list:
        #returns True if command in list
        return True

    else:
        #returns False if command not in list
        return False
