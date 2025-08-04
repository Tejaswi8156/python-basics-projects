# We can print a range of list items by specifying where we want to start, where we want to end, and if we want to skip elements in between the range.
# SYNTAX -> List[start:end]


# Printing Elements within a particular Range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes


# Printing all elements from a given index till the end
animalss = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animalss[4:])  # using positive indexes
print(animalss[-4:])  # using negative indexes


# Printing all elements from start to a given index
animal = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animal[:6])  # using positive indexes
print(animal[:-3])  # using negative indexes



#print(animals[::2])
# This is a slice with:
# Start: not specified (so it defaults to index 0)
# End: not specified (so it goes till the end of the list)
# Step: 2 (means take every 2nd item)

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes


# print(animals[-8:-1:2])
# This slice uses negative indexing:
# Start: -8 → index 1 (i.e., "dog")
# End: -1 → index 8 (i.e., up to but not including "cow")
# Step: 3

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])