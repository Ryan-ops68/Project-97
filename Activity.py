import random
number = random.randint(1,9)
chances = 0
while chances<5:
    limit = int(input("Enter a guess number"))
    if (limit==number):
        print("Well done")
    elif (limit>number):
        print("Your guess was too high")
    else:
        print("You guess was too low")
    chances+=1
if not chances<5:
    print("You lose number was ", number)
