# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
name = input("What is your name?: ")

# TODO: Ask the user for their age and store it in a variable
age = input("What is your age?: ")

# TODO: Print a greeting using the name and age variables
print("Hello " + name + " you are " + age + " years old. ")

#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
length = int(input("What is the length of a rectangle?: "))
length = int(length)

# TODO: Ask the user for the width of a rectangle and store it as an integer
width = input("What is the width of a rectangle?: ")
width = int(width)

# TODO: Calculate the area of the rectangle
area = int(length) * int(width)

# TODO: Print the result
print(area)

#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
temperature = input("What is the temperature in celsius?: ")
temperature = float(temperature)


# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
Fahrenheit = (temperature * 9/5) + 32

# TODO: Print the result rounded to two decimal places
print(round(Fahrenheit, 2))

