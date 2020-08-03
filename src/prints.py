import os
import set_colors
import random
import checks
import time
import sys

#prints the welcome message
def print_welcome():

    which_print = random.randint(1, 2)

    if which_print == 1:

        try:
            #printing message for the user
            os.system("cowsay -f gnu Thanks for using Open-Shodan | lolcat")

        except Exception:
            #printing message for the user about cowsay and lolcat
            print(set_colors.C_MAGENTA + "For the full experience of Open-Shodan install cowsay and lolcat")

    elif which_print == 2:
        try:
            #printing the message for the user
            os.system("figlet OPEN-SHODAN | lolcat")

        except Exception:
            #printing message for the user about figlet and lolcat
            print(set_colors.C_MAGENTA + "For the full experience of Open-Shodan install figlet and lolcat")

    #print motivation quote from Master Yoda
    print(set_colors.C_YELLOW + "\nDo it or don't do it. There is no trying. ~Master Yoda\n------------------------------------------------------")

    #print help command if someone is new to Open-Shodan
    print("You don't know the commands? Use 'help'\n")


#prints the help about the commands
def print_help():

    explanation_list = ["Search for a IP",
                   "Search for a Keyword",
                   "Get the help you are reading right now",
                   "Quit the program"]

    for command in checks.command_list:
        for explanation in explanation_list:

            print(set_colors.C_YELLOW + command + " ---> " + explanation)



#prints the empty key message
def no_key():

    #print message
    print(set_colors.C_YELLOW + "Please set the API to use Open-Shodan\nContact us on Github")


#print loading
def loading():

    sys.stdout.write('['+' '*10+']  0%')
    sys.stdout.flush()

    for i in range(10):
        time.sleep(0.2)
        sys.stdout.write('\b'*(15-i) + '=')

        if(i < 9):
            sys.stdout.write('>')
        sys.stdout.write(' '*(8-i) + '] ' + str(i+1) + '0%')
        sys.stdout.flush()

    sys.stdout.write('\b\b\b\bDone!\n')
