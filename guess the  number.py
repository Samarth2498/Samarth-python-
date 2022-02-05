# Test 123
import random
randnumber = random.randint (1,100)
userguess = None
guesses = 0
chances = 10
while(userguess != randnumber):
    userguess = int(input("pls Enter your guess "))
    guesses  += 1
    if (userguess == randnumber):
     print("your guess is right!")
    else:
        if (userguess>randnumber):
          print("you guessed it wrong! Enter a smaller number")  
        else:
            print("you guessed it wrong! Enter a larger number")


    

            

        
print(f"you guessed the number in {guesses} guesses")
