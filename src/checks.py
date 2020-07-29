import os
import sys

global command_list

command_list = ["sip", "srch", "help", "quit"]


#checks if inputed command is in command_list
def check_command(cmd_str):

    #checks list and parameter
    if cmd_str[0] in command_list :

        #checks if command is help or quit so its not spotted as wrong
        if cmd_str[0] == "help" or cmd_str[0] == "quit":

            #returns True because it does not have a parameter
            return True

        #checks if command has parameters and that the parameter is not empty
        elif len(cmd_str) == 2 and cmd_str[1] != "":
            #returns True if command has parameters and its not empty
            return True


    else:
        #returns False if command not in list
        return False
