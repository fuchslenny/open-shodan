import shodan
import sys
import search_ip
import set_colors
import os



#database integration for safety about reverse engineering
API_KEY = "MhalN3iyvINULCeGPcweV1Kfz6jIxZLs"

#main functions calls other functions
def main():

    #call the login functions for connecting to the api
    api = login()

    while not api[1]:
        print("waiting for api")
        sleep(1)

    menu()


#performs the login with the api_key
def login():

    #make connection
    api_con = shodan.Shodan(API_KEY)

    #return the api_key
    return api_con, True


#select menu for different options
def menu():

    #printing message for the user
    os.system("cowsay -f gnu Thanks for using open-shodan | lolcat")

    print(set_colors.C_GREEN + "\nHow can I help you my Master\n----------------------------------------\n")

    print("you don't know the commands? use the ->help<- command")


#calling the main function
if __name__ == "__main__":
    main()
