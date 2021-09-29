#Simple Function
def greet():
  print("Hello Samyam")
  print("How do you do Rachel Rach?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Rachel Rach' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Rachel Rach")

#Functions with more than 1 input
def greet_with(name, location):     #  Function with two parameter.
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Rachel Rach", "Nowhere")             # The first argument gets assigned to 1st parameter and 2nd to 2nd parameter.
#vs.
greet_with("Nowhere", "Rachel Rach")


#Calling greet_with() with Keyword Arguments
greet_with(location="Bhaktapur", name="Samyam")