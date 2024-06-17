#from random import choice
import random

#flip a coin
#coin = ["heads", "tails"]

#print(choice(coin))

#choose an int inbetween two numbers
number = random.randint(1,10)
print(number)

#shuffle: takes a list and shuffle it

cards = ["jack", "queen", "king"]

random.shuffle(cards)
for card in cards:
    print(card)

