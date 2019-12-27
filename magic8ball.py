import time
import random

while True:
    #List of answers
    alist = ["Yes","No","Maybe","Wait and see","Best not to answer now","Probably",
            "There is a possibility", "The odds are in your favor", "Probably not",
            "The future is still cloudy", "Not sure", "Maybe tomorrow", "Not today",
            "Good luck with that", "You can certainly try",
            "How do you want to do this", "Wouldn't you like to know, weather boy",
            "It'll end in cake", "Who cares?", "42"]

    input("Enter a question: ")

    #"In progress" statement
    for i in range(5):
        print("Thinking...")
        time.sleep(1)

    print("\n")

    #Print randomized answer
    print("Answer: " + str(alist[random.randint(0, 19)]))

    #Check if user wants to reset the question loop
    answer = input("Would you like to ask another question? Answer with y for Yes or n for No. \n")

    if answer == "y":
        pass
    elif answer == "n":
        break
    else:
        print("Please enter a valid answer.")
