#test All function
#Print
#print("Hello world")

a = 10
b = 20
#condition
def iftest():
  if a > b:
    print(" A is more")
  else: 
    print(" B is right")

def myfunc():
  x = "Fantastix"
  print(" Python is " + x)

#myfunc()

#List

thislist = ["apple","banana","cherry"]
thatlist = ["red","green","yellow"]
#print(thislist[-2])

thistuple = ("apple" ,"banana","mango")
#print(listlist[-4:-1])
thisset = {"apple","banana","orange"}

thisdict = {
  "brand":"Ford",
  "model":"Mustang",
  "year": 1964 }
# print(len(listlist))
# thislist.append("orange")

#Loop
# i = 0
# while i <6:
#   i += 1
#   if i == 3:
#     # break
#     continue
#   print(i)

# for x in thislist:
#   for y in thatlist:
#   print(x , y)

# Recursive
# def recurtest(l):
#   if l > 0:
#     result = 5 * recurtest(l-1)
#     print(result)
#   else :
#     result = 1
#   return result

# recurtest(3)

user = input("Enter user :")
print("username is : " +user)