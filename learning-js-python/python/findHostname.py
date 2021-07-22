import socket

arr = []

def readfile():
    with open('../resources/known.hosts') as my_file:
        for line in my_file:
            arr.append(line.replace("\n", ""))

def findHostname(hostname):
    for x in arr:
        if x == hostname:
            return True
    return False

def main():
    hostname = socket.gethostname()
    print(hostname)

    readfile()
    print(arr)

    found = findHostname(hostname)
    if found == True:
        print('Hostname found!')
    else:
        print('Hostname NOT found!')

main()