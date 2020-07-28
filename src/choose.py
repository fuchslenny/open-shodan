import shodan_actions
import sys
import checks
import prints


#decides what is called next
def decide(cmd_str, api):

    #if command is sip calls search ip function
    if cmd_str == "sip":
        shodan_actions.search_ip(api)

    #if command is help calls help function to print infos
    elif cmd_str == "help":
        prints.print_help()
    
    else:
        exit(1)
