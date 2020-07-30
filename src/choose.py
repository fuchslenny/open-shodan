import shodan_actions
import sys
import checks
import prints


#decides what is called next
def decide(cmd_str, api):


    #if command is sip calls search ip function
    if cmd_str[0] == "sip":
        shodan_actions.search_host(api, cmd_str[1])

    #if command is help calls help function to print infos
    elif cmd_str[0] == "help":
        prints.print_help()

    #if command is srch calls search function
    elif cmd_str[0] == "srch":
        shodan_actions.search(api, cmd_str[1])

    #if command is quit calls quit function to close program
    elif cmd_str[0] == "quit":
        shodan_actions.quit_program()
