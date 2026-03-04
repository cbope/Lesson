# Pangolins!

knowledge = {"Does it live in the sea?" : "Whale", "Does it eat ants?" : "Pangolin", "Does it have a shell?" : "Turtle", "Does it have a trunk?" : "Elephant"}

def ask_question():
    found = False
    for question in knowledge:
        print("Answer Y/N")
        response = input(question)
        if(response.upper() == "Y"):
            found = True
            break
    if found:
        print("I thought so!")
    else:
        print("I don't know.")
        new_animal = input("What animal is it? ")
        new_question = input("Tell me something about a " + new_animal + " in the form of a question: ")
        knowledge[new_question] = new_animal

def play():
    key = input("Think of an animal. Press enter when you are ready.")
    ask_question()

def __main__():
    ok = True
    while (ok):
        play()
        response = input("Do you want to play again? (Y/N) ")
        if response.upper() == "N":
            ok = False
        if response.upper() == "Y":
            ok = True

if (__name__ == "__main__"):
    __main__()