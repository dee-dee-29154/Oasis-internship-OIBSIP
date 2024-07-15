import tkinter as tk
import random
import string
import pyperclip  # Ensure you have pyperclip installed: pip install pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "Error: At least one character type must be selected."

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def generate():
    length = int(length_entry.get())
    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    result_label.config(text=f"Generated Password: {password}")
    pyperclip.copy(password)  # Copy to clipboard

# Setting up the GUI
app = tk.Tk()
app.title("Random Password Generator")

tk.Label(app, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(app, text="Include Letters", variable=letters_var).grid(row=1, columnspan=2)
tk.Checkbutton(app, text="Include Numbers", variable=numbers_var).grid(row=2, columnspan=2)
tk.Checkbutton(app, text="Include Symbols", variable=symbols_var).grid(row=3, columnspan=2)

generate_button = tk.Button(app, text="Generate Password", command=generate)
generate_button.grid(row=4, columnspan=2)

result_label = tk.Label(app, text="")
result_label.grid(row=5, columnspan=2)

app.mainloop()
