import os
import set_colors
import random

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
    print("You don't know the commands? Use ->help<-\n")


#prints the help about the commands
def print_help():

    print("Coming soon ...")
