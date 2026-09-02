print("===== BMI CALCULATOR =====")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than 0.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter numeric values.")

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n===== RESULT =====")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")