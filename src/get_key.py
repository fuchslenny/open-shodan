

#reads the file to get the shodan api key from the user
def read_file():

    #opens the file in read mode
    file = open("mykey.txt", "r")

    #reads the content
    api_key = file.read()

    #returns the key
    return api_key
