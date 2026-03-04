# This is a program that will get a name and add 'is cool' at the end.
#Chris Bope
#3/3/2026

def coolify(name):
    return name + " is cool"


def __main__():
    myname = input("Please type your name: ")
    myname = coolify(myname)
    print(myname)