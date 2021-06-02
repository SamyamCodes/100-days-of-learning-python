
year = int(input("Which year do you want to check? "))

#Write your code below this line 👇
if year%4 ==0:
  if year%100==0:
    if year%400==0:
      print("The year is leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("The year is not a leap year")

     
     





