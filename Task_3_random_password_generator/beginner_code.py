import random
import string


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


def main():
    try:
        length = int(input("Enter desired password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        if length < 1:
            print("Password length must be at least 1.")
            return

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for length.")


if __name__ == "__main__":
    main()
