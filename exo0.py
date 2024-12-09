import math


numberOfPeople = int(input("How many people are you? "))
numberInOneTaxi = int(input("How many people can fit in one taxi? "))
print("You will need", math.ceil(numberOfPeople /numberInOneTaxi), "taxis.")
