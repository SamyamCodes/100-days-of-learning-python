# Python uses pemdas rule
# ** is used for expinentials.
print(2**3) # This is equivalent to 2 to the power 3.
# type() shows data type.
# str(len(nae_1)) converts the data of integer to string.
# pemdas = parenthesis, exponential, multiplication, division, addition, subtraction from left to right

print(3*3 +3/3 -3)
#  3*3 =9 and 3/3 =1 and 10-3 =7

weight =input("Enter yoy weight in kg, m: ")
height =input("Enter yout heugh in meter, h: ")

bmi = int(weight)/ float(height)**2 # Here, we simply cant write height**2 without converting to float  as it is a string
bmi_as_int = int(bmi)
print(bmi_as_int)


# round() is used for rounding of the data value.
print(round(8/3, 2)) # this rounds upto 2 decimal value. here, answer is 2.67
print(round(8/3)) # answer is 3
print(8//3) # // is floor division. It makes result directly in integer. answer is 2.
# Remember, 4/2 is by default float in python. Ans is 2.0
result=4/2
result/=2
print(result) # Ans is 1.0

# f-string makes printing of string and integer posssible in a single line. Keep f outside" " but before string.
score=0
height=1.8
isWinning=True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
# Output is  Your score is 0, your height is 1.8, you are winning is True

# This program prints the sum of two numbers. eg input =38, output = 3+8 =11
two_digit_number = input("Type a two digit number: ")
#Check the data type of two_digit_number
print(type(two_digit_number))
#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
#Add the two digits togeter
two_digit_number = first_digit + second_digit
print(two_digit_number)

# This code prints your remaining life in days , years, and months.
age = input("What is your current age?")
age_as_int = int(age)
years_remaining= 90-age_as_int
days_remaining= years_remaining*365
months_remaining= years_remaining*12
weeks_remaining=years_remaining*52
message=f"You have {days_remaining}days, {years_remaining}years, {weeks_remaining}weeks, and {months_remaining} months left."
print(message)

# This code calculates the bill for each person. 
print("Welcome to thetop calculator")
total_bill = float(input("What was the total bill? $ "))
percent= int(input("What percent tip would you like to give? 10, 12, or 15? "))
people= int(input("How many people to split the bill?"))
tip_as_percent= percent/100
total_tip= total_bill* tip_as_percent
final_bill = total_bill + total_tip
bill_per_person= final_bill/people
final_amount=round(bill_per_person, 2)
final_amount= "{:.2f}" .format(bill_per_person)
print(f"Each person should pay: $ {final_amount}")

# Output is
Welcome to thetop calculator
What was the total bill? $ 200
What percent tip would you like to give? 10, 12, or 15? 10
How many people to split the bill?4
Each person should pay: $ 55.00










