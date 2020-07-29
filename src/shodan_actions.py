import shodan
import sys
import set_colors
import socket


#search for specific ips
def search_ip(api, cmd_str):

    ip = cmd_str[1].strip()

    try:
        #check if ip address is valid by looking for a
        socket.inet_aton(ip)

    except Exception:
        #if exception is thrown the ip is invalid
        print(set_colors.C_YELLOW + "INVALID IP ADDRESS")


#normal api search
def search(api, cmd_str):

    try:
        # search for the key word that was inputed
        search_res = api.search(cmd_str[1])

        for result in search_res['matches']:
            print(set_colors.C_YELLOW + "IP: {}".format(result["ip_str"]))
            print(set_colors.C_WHITE + result["data"])
            print(set_colors.C_RED + "\n----------------------------------------------\n")

    except shodan.APIError:
        print(set_colors.C_YELLOW + "It appeared a API Error please check your API Key")




#quits the program if  called
def quit_program():
    #last mesage before quitting the program
    print(set_colors.C_YELLOW + "See you next time young Padawan")
    exit(1)
