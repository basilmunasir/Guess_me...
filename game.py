import random

secret_number=random.randint(1,50)
print("I Guessed a number between 1 and 50,can you predict it??\nYou Got 5 try")
flag=0

for guess_taker in range(5):
    guess=int(input("Guess : "))

    if(guess>secret_number):
        print(guess," is high maaahn \n",4-guess_taker," chances remaining")
    elif(guess<secret_number):
        print(guess," is low maaahn \n",4-guess_taker," chances remaining")
    else:
        print("Congratulation ",guess," is the correct one.\nYou find it within ",guess_taker+1," try")
        flag=1
        break

if(flag==0):
    print("Ooo So close, Leave it we will crack it next time.")
    print("The number i guessed is : ",secret_number)
