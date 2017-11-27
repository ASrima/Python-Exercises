#We can create dictionaries using brcaces{}
a = dict (one=1, two=2, three = 3)
b = {"one": 1, "two" :2, "three" : 3}
c = dict(zip(["one","two","three"],[1,2,3]))
d = dict ([("two",2),("one",1),("three",3)])

e = dict({"three":3,"one":1,"two":2})
print(a)
print(b)

#Create a List
list1 = ['physics','chemistry','biology','history','psychology']
list2 = [1,2,3,4,5,6,7]
print (list1[3],list1[4])
print(list2[1:2],list2[1:5])

#Using operators in lists
list1 = [123,"New York","Boston","Michigan","New Jersey"]
list2 = [235,"Ryan","color","football"]
print("First list length is : ", len(list1))
print("Second list length is : ", len(list2))
print(list1 +list2) #prints both the lists in a single line

print((list1 * 3)+(list2 * 2))  # Prints list one 3 times and list2 2 times
