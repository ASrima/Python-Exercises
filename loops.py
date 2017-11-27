words =["cat","dog","bunny","breeze"]
for w in words:
    print(w, len(w))

# Another example of loop

primes = [2,3,4,5,7]
for prime in primes:
    print(prime)


# One more example of for loop

for count in (1,2,3,4,5):
    print("Down")
    print("up")
    print(count)
    print("yes" * count)


#  Example of for loops

for count in (1,2,3,4,5,6):
    print("down")
    print("up")
    print(count)
    print("yes" * count)
    print("Done counting")
for color in("red","blue","green","black"):
    print(color)


# example of while loop
#prints out 0,1,2,3,4
'''
while loop simply repeats as long as a
certain boolean condition is met
'''
count = 0
while count<5:
    print(count)
    count+=1 '''if count+ =1 is not used it will be an infinite
    loop as 5 is always less than 0 and it will keep printing zeros'''
    

#example of how to break a loop
    
count  = 0
while True:
    print(count)
    count+=1
    if count >=5:
        break
