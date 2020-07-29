import shodan
import sys
import shodan_actions
import set_colors
import os
import choose
import prints
import time
import checks
import get_key


#main functions calls other functions
def main():

    #get the key
    API_KEY = get_key.read_file()


    #call the login functions for connecting to the api

    api = login(API_KEY)

    time.sleep(1)

    #prints the welcome message
    prints.print_welcome()

    time.sleep(1)
    menu(api)


#performs the login with the api_key
def login(key):

    #make connection
    api_con = shodan.Shodan(key)

    #return the api_key
    return api_con


#select menu for different options
def menu(api):

    try:
        #get input what user wants
        tmp_opt = str(input(set_colors.C_RED + "--> "))

    except KeyboardInterrupt:
        exit(1)

    #split the command in option and parameters
    command = tmp_opt.rsplit(" ")

    #checks if user inputs is in command list
    checked = checks.check_command(command)

    #checks checked value
    if checked == True:
        #sends choice at choose.py if command is right
        choose.decide(command, api)
        menu(api)

    else:

        #if checked command is false return to menu and output thats a wrong command
        print(set_colors.C_YELLOW + "NOT A VALID COMMAND MY PADAWAN")

        menu(api)



#calling the main function
if __name__ == "__main__":
    main()
