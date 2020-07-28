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
        tmp_opt = str(input())

    except KeyboardInterrupt:
        exit(1)

    #checks if user inputs is in command list
    checked = checks.check_command(tmp_opt)

    if checked == True:
        #sends choice at choose.py if command is right
        choose.decide(tmp_opt, api)
        menu(api)

    else:
        menu(api)



#calling the main function
if __name__ == "__main__":
    main()
