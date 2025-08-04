# Escape Characters are very important in Python. They allow us to insert illegal characters into a string, such as a backslash, new line, or a tab.
#used to insert single/double quotes in the string.
str1 = "He was \"Flabergasted\"."
str2 = 'He was \'Flabergasted\'.'
print(str1)
print(str2)


#inserts a new line wherever specified
str3 = "I love doing Workout. \nIt refreshes my mind and body."
print(str3)

#inserts a tab(    ) wherever specified.
str4 = "Hello \t\tWorld \t!!!"
print(str4)


#erases the character before it wherever it is specified.
str5 = "Hello  \bWorld !!!"
print(str5)


#used to insert a backslash into a string
str3 = "What will you eat? \n->Apple\\Banana"
print(str3)