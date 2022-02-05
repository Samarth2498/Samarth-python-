import random
comp = random.randint(1,3)
print(comp)
you = int(input("rock(1),paper(2),siccor(3): "))
if comp == you:
    print("you tie")
# computer possiblities
if comp == 1  and you == 3:
     print("you lose because computer did",comp) 
elif comp == 2 and you == 1:
    print("you lose because computer did",comp)
elif comp == 3 and you == 2:    
    print("you lose because computer did",comp)
# my possiblities  
if comp == 3 and you == 1:
    print("you win because computer did",comp)
elif comp == 1  and you == 2:    
    print("you win because computer did",comp)
elif comp == 2  and you == 3:
    print("you win because computer did",comp) 