str1 = "Tejaswi"
print(str1.upper())
print(str1.lower())

str2 = "   Silver Spoon    "
print(str2.strip())


str3 = "Hello !!!"
print(str3.rstrip("!"))

str4 = "Silver Spoon"
print(str4.replace("Sp", "M"))


str5 = "Silver Spoon"
print(str5.split(" "))

str6 = "tejaswi"
capstr6 = str6.capitalize()
print(capstr6)

str7 = "Tejaswi kumar Chaturvedi"
center = str7.center(50)
print(str7.center(50, "."))

str8= "tejaswi kumar chaturvedi"
print(str8.count("a"))

str9 = "Welcome to the Console !!!"
print(str9.endswith("!!!"))

str10 = "His name is Dan. Dan is an honest man."
print(str10.index("Dan"))