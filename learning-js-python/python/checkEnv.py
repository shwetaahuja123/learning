import sys

def identifyEnv():
    filename = sys.argv[0]

    if ".py" in filename:
        print("I am python")

identifyEnv()