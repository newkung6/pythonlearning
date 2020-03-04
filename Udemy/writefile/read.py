# path = ""
# ff = open("/Users/Nsan/code/Pytontest/Udemy/Testtext.txt","r+")
# # ff = open("C:\\Users\\Nsan\\code\\Pytontest\\Udemy\\Testtext.txt","a+")
# # ff.write("Hi test text\n")

# for i in ff:
#     print(i,end="")
# ff.close
# print("TestEnd")


# with open("/Users/Nsan/code/Pytontest/Udemy/Testtext.txt", 'r') as jabber:
#     for line in jabber:
#         print(line,end="")

with open("/Users/Nsan/code/Pytontest/Udemy/Testtext.txt", 'r') as jabber:
    lines = jabber.readline()  
print(lines)
print("firse")

for line in lines[::-1]:
    print(line, end="")

print("second")

with open("/Users/Nsan/code/Pytontest/Udemy/Testtext.txt", 'r') as jabber:
    lines = jabber.read()

print("third")

for line in lines[::-1]:
    print(line, end="")