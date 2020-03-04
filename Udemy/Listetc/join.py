myList = ["a","b","c","d"]

newString = ", ".join(myList)
# for c in myList:
#     newString += c + ", "

print(newString)


location = {0:"You are sitting in front of a computer learning Python",
            1:"You are standing at the end of a road before a small brick building",
            2:"You are at the top of a hill",
            3:"You are inside a building, a well house for a samll steam",
            4:"You are in a valley beside a steam ", 
            5:"You are in the forest",
            }

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "S": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    availableExits = ""
    for direction in exits[loc].keys():
        availableExits += direction + ", "
    
    print(location[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExits).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")