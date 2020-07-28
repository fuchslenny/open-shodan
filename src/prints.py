import os
import set_colors
import random

#prints the welcome message
def print_welcome():

    which_print = random.randint(1, 2)

    if which_print == 1:

        #printing message for the user
        os.system("cowsay -f gnu Thanks for using open-shodan | lolcat")

    elif which_print == 2:

        #printing the message for the user
        os.system("figlet OPEN-SHODAN | lolcat")

    print(set_colors.C_GREEN + "\nHow can I help you my Master\n----------------------------------------\n")

    print("you don't know the commands? use the ->help<-")


#prints the help about the commands
def print_help():

    for i in checks.command_list:
        print(i + "\n")
