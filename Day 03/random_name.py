'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
'''

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

num_items = len(names)
# Generate random numbers between 0 and the last index.

random_choice = random.randint(0, num_items - 1)

# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

