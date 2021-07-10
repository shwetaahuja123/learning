import ast

def initialize():
    file = open("src/utilities/authDetails.txt", "r")

    contents = file.read()
    dictionary = ast.literal_eval(contents)

    file.close()
    return dictionary

users = initialize()