# this program is basic
name = input("Enter your name: ")
length = len(name)
surname = input("Enter your surname: ")
length1 = len(surname)
# this code lines are for displaying the value in reverse way
change = name
name = surname
surname = change

#here, str() lets us to convert inteher to string .
print("Your name has " + str(length) + 'words')
print("Your surname has " + str(length1) + 'words.')
print("Your surname is: " + name)
print("Your name is: " + surname)

print(' e.g. we can use print "+" to d')