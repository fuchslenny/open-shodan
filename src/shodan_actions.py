import shodan
import sys
import set_colors


#search for specific ips
def search_ip(api, cmd_str):
    pass


#normal api search
def search(api, cmd_str):
    print(set_colors.C_YELLOW + cmd_str)

    """
    search_res = api.search(search_str)

    print(search_res)
"""


#quits the program if  called
def quit_program():
    #last mesage before quitting the program
    print(set_colors.C_YELLOW + "See you next time young Padawan")
    exit(1)
