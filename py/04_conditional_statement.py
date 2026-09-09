weight_kg = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# cm change to meter
height_m = height_cm / 100

while True:
    try:
        bmi = weight_kg / (height_m ** 2)
        if bmi < 18.5:
            print("Under weight")
            break
        elif bmi < 24.9:
            print("Normal weight")
            break
        elif bmi < 29.9:
            print("Over weight")
            break
        else:
            print("Obese")
            break
    except ValueError:
        print("Invalid input")
        continue
        break

print(f"{bmi:.2f}")
