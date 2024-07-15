def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from cm to m
    return weight / (height_m ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))

        if weight <= 0 or height_cm <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height_cm)
        category = classify_bmi(bmi)

        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
