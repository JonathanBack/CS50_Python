'''
i = 0
while i < 3:
    print("hi")
    i += 1


for _ in range(3):
    print("meow")

#you can change i -> _ it just shows that the variable wont be further used

print("meow\n" * 3, end ="")

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")
main()
