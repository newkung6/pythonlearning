# even = set(range(0, 40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4, 6, 9, 16, 25)
# square = set(squares_tuple)
# print(square)
# print(len(square))

# print(even.union(square))
# print(len(even.union(square)))

# print(square.union(even))
 
# print("-" * 40)

# print(even.intersection(square))
# print(even & square)
# print(sorted(square.intersection(even)))
# print(square & even)

textin = input("put sometext : ")
text = set(textin)
vowel_tuple = ('a' , 'e', 'i', 'o', 'u')
vowel = set(vowel_tuple)
lists = []

print(sorted(text.difference(vowel)))

# for word in text:
#     if word not in vowel:
#         text.discard(word)
    
print(lists)