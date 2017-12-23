#An adventure game of two friends

username = input("Tell us your name to start the Adventure : ")
friend =input("Tell us your friend name with whom you wanna on this exciting Adventure: ")

print("\n")
print("Awesome! Since %s and %s have decided to go on an adveture I am gonna start the story of their adventure " %(username, friend))
print("SO since exams are over and %s and %s have nothing better to do they made a list of things they want to do."%(username, friend))
print(" They both could not decide which one they should start first from the list.")
print("Even though %s wanted to sit at home and relax %s was being persistant to go for bungee jumping or skydiving. " %(username, friend))
print("But they both were  confused which one to start first.")
print("Do you have any suggestions for them?")
stranger = int(input("Enter 1: "))
if stranger ==1:
    print("Great! Tell us which one you think they should try first.")
    print("If you want them to go for bungee jumping first then enter '1.'")
    print("But if you want them to go for skydiving first then enter '2.'")
    print("\n")

    adventure = int(input("Which one they should do first?"))
    if adventure ==1:
   

        print("So they decided to go to Bronx Zoo for bungee jumping as %s lives in Bronx they both decided to go to the Bronx Zoo one first" %(friend))
        print("They both purchase tickets but %s was very scared as %s has never tried bungee jumping before and was thnking of going back." %(username, username))
        print("On the other hand %s also never tried bungee jumping before and was excited to try it so %s made %s start the adventure!." %(friend,friend,username))
        print("After that they went for lunch and strated to plan their next adventure.")
        print("%s  suggested they should go to Coney Island beach as %s loves to walk on the beach shore and enjoyes talking about life while walking on boardwalk." %(username,username))
        print("%s said they could also to a park and enjoy the weather and have ice cream" %(friend))
        print("%s %s both decide they should also invite their other friends to join them for lunch so that all of them could enjoy together."%(username,friend))
        print("\n")
        print("Which one you think they should do first?")
        print("If you think they should do what %s has suggested then type '1.'" %(username))
        print("If you think they should do what %s has suggested then type '2.'" %(friend))

        beach = int(input("So what do you think? "))
        if beach==1 or beach==2:
                print("They went to the park bought ice cream and made paper boats and gave them to kids who were in the park to play with them.")
                print("So they went to the beach and started to walk on the shore. While they are walking %s suddenly strated to feel sick" %(username))
                print("%s wanted to go home and cancel the plan for the day :(." %(username))
                print("What do you think %s should take %s to hospital and drop %s home or leave %s and go home?" %(friend,username,username,username))
                print("Choose 1 if you think %s should leave %s to go home alone and not to take %s to doctor." %(friend,username,username))
                print("Choose 2 if you think %s should take %s to the hospital and drop %s home safely." %(friend,username,username))

                choice = int(input("Make choice wisely!"))
                if choice==1:
                    print("That's rude. A true friend would never do that and %s would definately take %s to the hospital and drop home safely." %(friend,username))
                    print("It's not fun playing the adventure game with you. The game is over!.")
             
                elif choice==2:
                      print("Yes %s should do that because a friend in need is a friend indeed!" %(friend))
                else:
                      print("Invalid input. Did you enter 1 or 2.")
   

    
            
                      print("You did not enter a valid input. Do you wannna try again?")
                      print("If you wanna try again then you can start again by running 'python adventure.py' another time at the prompt.")

    elif adventure ==2:
          print("They both decided to go for skydiving but %s did not have enough money and therefore decided not to try it now" %(friend))
          print("%s offered %s to help and buy tickets for both but %s insisted they try it next time and maybe for now they could go to the park" %(username,friend,friend))
       
      # print("They both decided to go for skydiving but %s did not have enough money and therefore decided not to try it now" %(username))
      # print("%s offered %s to help and buy tickets for both but %s insisted they try it next time and maybe for now they could go to the park" %(friend,username,username))
             
               
else:
    print("The weather is bad outside it's better to stay at home and get bored")


    


      

