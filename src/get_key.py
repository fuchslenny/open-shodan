

#reads the file to get the shodan api key from the user
def read_file():

    #opens the file in read mode
    file = open("mykey.txt", "r")

    #reads the content
    api_key = file.read()

    key = api_key.replace(" ", "")

    #returns the key
    return key
