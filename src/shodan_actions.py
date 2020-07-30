import shodan
import sys
import set_colors
import checks


#search for specific ips
def search_host(api, cmd_str):

    #deletes the whitespaces from string
    ip = str(cmd_str[1].strip())

    #checks the ip if it valid
    check_ip = checks.check_ip(ip)

    #only look for host if ip is valid
    if check_ip == True:

        try:


            #look for the host and gather information via api
            check_host = api.host(ip)

            #print information about the host
            print(set_colors.C_YELLOW + """IP: {}
                                           OS: {}
                                           Organization: {}
                                           Vulnerabilities: {}""".format(check_host['ip_str'],
                                            check_host.get('os', 'n/a'), check_host.get('org', 'n/a'), host))

            #print further information
            for i in check_host["data"]:
                print("""Port: {}
                         Banner: {}
                            """.format(i["port"], i["banner"]))

        #except an Error if one occured
        except Exception as ex:

            #print error message
            print("[-] Error: " + str(ex))






#normal api search
def search(api, cmd_str):

    try:
        # search for the key word that was inputed
        search_res = api.search(cmd_str[1])

        print("[*] Loading...")

        for result in search_res['matches']:
            print(set_colors.C_YELLOW + "IP: {}".format(result["ip_str"]))
            print(set_colors.C_WHITE + result["data"])
            print(set_colors.C_RED + "\n----------------------------------------------\n")

    except Exception as e:
        print(set_colors.C_YELLOW + "Error: " + str(e))




#quits the program if  called
def quit_program():
    #last mesage before quitting the program
    print(set_colors.C_YELLOW + "See you next time young Padawan")
    exit(1)
