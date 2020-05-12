import random

S = random.randint(1, 20)
print(S)
chances=0

chan=int(input("How Many Chances"))
print(chan)

while chances<chan:
    num = int(input("Enter a value: "))
    print(num)

    if num==S:
        print("You Won")
        break
    elif num>S:
        print("GO LOWER!")
    else:
        print("GO HIGHER")

    chances +=1

if not chances < chan:
    print("YOU LOSE!!! The number was", S)


