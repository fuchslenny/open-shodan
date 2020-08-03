import prints
import sys

#reads the file to get the shodan api key from the user
def read_file():

    #opens the file in read mode
    file = open("mykey.txt", "r")

    #reads the content
    api_key = str(file.readline())

    #delete whitespaces
    key = api_key.strip()

    #check that there is a key
    if key != "":

        #returns the key
        return key

    #if key is empty print that the key must be set
    else:

        #call print function
        prints.no_key()

        exit(1)
