import shodan
import sys
import set_colors


#search for specific ips
def search_ip(api):

    #user input
    try:
        inp = str(input())

    except KeyboardInterrupt:
        exit(1)

    try:

        # Perform the search
        query = ' '.join(inp)
        search_res = api.search(query)

        # Loop through the matches and print each IP
        for service in search_res['matches']:
                print(service['ip_str'])

    except Exception as e:
        print(e)
        exit(1)
