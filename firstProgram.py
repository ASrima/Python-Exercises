#Ask for user name
name = input("What is your name? ")
print("Nice to meet you "+" "+name+ " !")
#Ask user for age
age=input("What is your age? " )
print("That's great " +name + ". Do you know how is the weather outside? ")
outside = str(input("You are going outside? "))

if outside == "yes": #Checks the condition based on the user input and tells what to do.
        print("Wear nice shorts :D ")
        print("Enjoy your day " +name+ "!")
else:
     print("You should go outside.")
     print("Life gets too boring when you stay at home for too long :P ")
