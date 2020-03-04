fruit = {"orange": "a sweet, orange, citurs fruit",
         "apple": "good for making cider" ,
         "lemon": "a sour yellow  citrus fruit",
         "grape": "a small, sweet fruit growing in bunche",
         "lime": "a sour , green citrus fruit"}

print(fruit)

veg = {"cabbage": "Every child's favourite",
        "sprouts":"mmmm , lovely",
        "spinach": "can iI Have some more fruit, please"}



print(veg)

veg.update(fruit)
print(veg)

# # for val in fruit.values():
# #     print(val)

# # print('-' * 40)

# # for key in fruit:
# #     print(fruit[key])

# # fruit_keys = fruit.keys()
# # print(fruit_keys)

# # fruit["tomato"] = "not nice with icecream" 
# # print(fruit_keys)

# print(fruit)
# print(fruit.items())
# f_tuple = tuple(fruit.items())
# print(f_tuple)

# for snack in f_tuple:
#     item,description = snack
#     print(item + " is " + description)

# print(dict(f_tuple))