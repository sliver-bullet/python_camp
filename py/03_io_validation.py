
print("roblox game login")
name = input("Enter your name: ")
height = int(input("Enter your height in cm: ")) 

# input validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 18 and age < 120:
            break
        elif age < 18:
            print("You are underage.")
            exit()
        else:
            print("Please enter a valid age!")
            exit()
    # except Exception as e: 
    #     print(f"An error occurred: {e}")
    except Exception as e: 
         print(f"An error occurred: {e}")


# Output validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} cm.")
print(f"You will able to start the game")