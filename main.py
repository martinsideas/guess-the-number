# A game to guess a number
import random

myAttempts = 0
maxAttempts = 6

print('Hi! My name is Christa. What is your name?')
myName = input()

a = 1
b = 20

randomNumber = random.randint(a, b)
print("Well, " + myName + ", My number is between " + str(a) +" and " + str(b))

while myAttempts < maxAttempts:
    print('Try guessing...')
    attempt = int(input())
    myAttempts = myAttempts + 1

    if attempt < randomNumber:
        print('Your estimate is lower')
    
    if attempt > randomNumber:
        print('Your estimate is higher')
    
    if attempt == randomNumber:
        myAttempts = str(myAttempts)
        print('Well done, ' + myName + '! You guessed my number in ' + myAttempts + ' tries!')
        break

if attempt != randomNumber:
    randomNumber = str(randomNumber)
    print('You lost. The number I was thinking of was ' + randomNumber)