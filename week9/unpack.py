    # usign .split is one way to unpack a value asigning it to more than one variable
'''
first, _ = input("what's your name? ").split(" ")
print(f"hello, {first}")
'''

    # unpacking values from a list
    # coins = [100, 50, 25]
    # *coins -> * means unpack a list
    # **coints
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# **coins is equal to -> galleons=100, sickles=50, knuts=25

#print(total(*coins), "Knuts")  #
print(total(**coins), "Knuts")  # passes all the keys and all the values
#print(*coins)   # unpack the list values into one individual value


def f(*args, **kwargs)
