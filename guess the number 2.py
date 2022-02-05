import random
randnumber = random.randint (1,100)
print(randnumber)
userguess = None
chances = 10
while(userguess != randnumber):
    userguess = int(input("pls Enter your guess "))
    chances -=  1
    if chances == 0: 
        if chances == 0 and userguess == randnumber:
          print("you guessed it right") 
          break
        elif chances == 0:    
             print("oops you ran out of chances")  
             break
    if (userguess == randnumber):
     print("your guess is right!")
    else:
        if (userguess>randnumber):
          print("you guessed it wrong! Enter a smaller number")
          print(f"you have {chances} guesses")  
        else:
            print("you guessed it wrong! Enter a larger number")
            print(f"you have {chances} guesses") 

          




    

            

        
