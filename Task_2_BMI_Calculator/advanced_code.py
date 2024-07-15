import tkinter as tk
from tkinter import messagebox


def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        height_m = height_cm / 100  # Convert height from cm to m
        bmi = weight / (height_m ** 2)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f} - {category}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight and height.")


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Setting up the GUI
app = tk.Tk()
app.title("BMI Calculator")

tk.Label(app, text="Weight (kg):").grid(row=0, column=0)
tk.Label(app, text="Height (cm):").grid(row=1, column=0)

weight_entry = tk.Entry(app)
height_entry = tk.Entry(app)

weight_entry.grid(row=0, column=1)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(app, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

result_label = tk.Label(app, text="")
result_label.grid(row=3, columnspan=2)

app.mainloop()
