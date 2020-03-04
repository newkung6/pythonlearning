
vocabulary = "hi popo this is test "
direction = ["a","e","i","o","u"]
for word in vocabulary:
    if word not in direction:
        print(word , end ="")

print("/n")
vocabulary = ["orange","apple","chompoo","tan","yelly"]
direction = ["chompoo","tan"]
for word in vocabulary:
    if word not in direction:
        print(word)