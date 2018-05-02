userString = input("Enter a string to reverse")
charlist = list(userString)
reversedString = ""
for char in reversed(charlist):
    reversedString += char
print(reversedString)
