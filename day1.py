name = input("Enter your name: ")
length = len(name)
surname = input("Enter your surname: ")
length1 = len(surname)
change = name
name = surname
surname = change


print("Your name has " + str(length) + 'words')
print("Your surname has " + str(length1) + 'words.')
print("Your surname is: " + name)
print("Your name is: " + surname)

print(' e.g. we can use print "+" to d')