import random
n = random.randint(1,100)
a = -1
guessess = 0

while(a != n):
    a = int(input("guess the number: "))

    if(a>n):
        print("lower number please")
        guessess += 1
    elif(a<n):
        print("higher number please")
        guessess += 1

print(f"you've guessed the number {n} correctly in {guessess} attempts")
print("or aap jeet chuke hai 7 crore apne delulu m")


