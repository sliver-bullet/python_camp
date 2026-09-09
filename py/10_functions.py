# Functions with parameters
def greet_person(name):
    print(f"Hello {name}")

greet_person("Alice")

# Functions with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)

# Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}"

print(greet_with_title("Smith"))        # "Hello, Mr. Smith"
print(greet_with_title("John", "Dr."))  # "Hello, Dr. Johnson!"

# Function with variable number of arguments
def greet_multiple(*names):
    for name in names:
        print(f"Hello, {name}")
greet_multiple("Alice", "Bob", "Charlie")


# multiple value and pass to argument at function
def sum_all(*args):
    return sum(args)
print(f"The total sum is: {sum_all(1,2,3,4,5)}") # Output: 15



# multiple key value and pass to argument at function
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="CK", age=40, city="PJ")


# Combine input argument and key value argument

def flex_function(*args, **kwargs):
    print(f"argument : {args}")
    print(f"key value argument: {kwargs}")

flex_function(1,2,3,4,5, name="CK", age=40, city="PJ")


# lambda function (anonymous function)
square = lambda x: x**2
print(square(5)) # Output: 25
print(square(8)) # Output: 64

add = lambda x, y: x + y
print(add(5, 3)) # Output: 8

# Exercises:
# Write the function to check if a number is prime
def is_prime(number):
    if number < 2 :
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Ouput
print("###Exercise 1###")
print(is_prime(7)) # Output: True
print(is_prime(10)) # Output: False

# Exercises:
# Build temperature converter (Celsius to Fahrenheit)
def celsius_to_fahrenheit(celsius):
    fahrenheit =  celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Output
print("###Exercise 2.1###")
print(f"25 C ={celsius_to_fahrenheit(25)} F")
print(f"77 F ={fahrenheit_to_celsius(77)} C")


# Exercises:
def temperature_converter():
    temp = float(input("Enter temperature: "))
    # change to upper case to prevent case sensitive
    unit = input("Enter unit (C for celsius, F for Fahrenheit): ").upper()
	
    if unit == "C":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}C = {result}F")
    elif unit == "F":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}F = {result}C")
    else:
        print("Invalid unit!")


print("###Exercise 2.2###")
temperature_converter()


