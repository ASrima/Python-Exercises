import random  #it will make the computer chose 

username = input("Tell us your name to start the Rock, Paper and Scissor game : ")
friend =input("Tell us your friend name with whom you wanna play this exciting game: ")
print("Awesome %s and %s ! We are about to start the game " %(username,friend))

print("\n")


def rps():# define rps ( stands for rock,paper, scissors)
    computer_choice =random.randint(1,3)
          
       #let the computer chose randomly
       #from the given 3 choices.  3 choices are for rock, paper and secissors. 1 for rock 2 for paper and 3 for scissor
    if computer_choice == 1:  #check the condition
                              

        computer_choice_rock() # it will run the rock program
    elif computer_choice == 2:  #check the condition

        computer_choice_paper() # it will run the paper program
        

    else:

        computer_choice_secissor()# it will run the scissor program if choice is not ==1 or ==2

def computer_choice_rock(): # defining the rock program
    user_choice = input(" Choice 1 is for rock, 2 is for paper and 3 is for scissor: ")
    if user_choice == "1": 
        print ("Its a tie %s. You choose rock and the computer chose rock" %(username))
        try_again()
    if user_choice == "2":
        print ("You win %s. You choose paper and the computer chose rock. Paper covers the rock" %(username))
        try_again()
    if user_choice == "3":  
        print ("You lose %s. You choose  scissor and the computer chose rock" %(username))
        try_again()
    else:
        print ("Try again")
        computer_choice_rock() # reruns the rock program
        
def computer_choice_paper():# defining the paper program
    user_choice = input("1 is for rock, 2 is for paper and 3 is for scissor: ")
    if user_choice == "1": 
        print ("You Lose %s. You choose rock and the computer chose paper" %(friend))
        try_again()
    if user_choice == "2": 
        print ("Its a tie %s. You choose Paper and the computer chose paper" %(friend))
        try_again()
    if user_choice == "3":
        print ("You win %s. You choose scissor and the computer chose paper. Scissor cuts the paper"%(friend))
        try_again()
    else:
        print ("Try again")
        computer_choice_paper()# reruns the paper program
        


def computer_choice_scissor():# defining the scissor program
    user_choice = input("1 for rock, 2 for paper and 3 for scissors: ")
    if user_choice == "1":
        print ("You lose. You choose Rock and the computer chose scissor")
        try_again()
    if user_choice == "2":
        print ("Its a tie. You choose scissor and the computer chose scissor")
        try_again()
    if user_choice == "3":
        print ("You win. You choose paper and the computer chose scissor")
        try_again()
    else:
        print ("Try again")
        computer_choice_scissor() # reruns the scissor program
def try_again(): # define try_again() function
    choice = input("Enter an input by  typing y or Y to play again: ")
    if choice == "y" or choice == "Y":
        rps()
    elif choice =="n":
        print ("Thanks for playing") #ends the program
        quit()
    else:
            print("Try again")
            try_again() # runs the try again loop again if the user dont enter y, Y or n
rps()
        
