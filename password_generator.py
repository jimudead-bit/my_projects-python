import random
import os


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"


def parse_number(prompt):
    """Ask the user for a number. Supports digits (12) and words (twelve, twenty one, one hundred)."""
    word_to_number = {
        "zero": 0, 
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4,
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 

        "nine": 9,
        "ten": 10, 
        "eleven": 11, 
        "twelve": 12, 
        "thirteen": 13,
        "fourteen": 14, 
        "fifteen": 15, 
        "sixteen": 16,
        "seventeen": 17, 
        "eighteen": 18, 
        "nineteen": 19,
        "twenty": 20, 
        "thirty": 30, 
        "forty": 40, 
        "fifty": 50,
        "sixty": 60, 
        "seventy": 70, 
        "eighty": 80, 
        "ninety": 90,
        "hundred": 100, 
        "thousand": 1000
    }

    def words_to_number(words):
        """Convert a list of number words to an integer."""
        total = 0
        current = 0
        for word in words:
            if word == "and":
                continue  
            if word not in word_to_number:
                raise ValueError(f"Unrecognized number word: {word}")
            value = word_to_number[word]
            if value >= 1000:
               
                total += (current + (1 if current == 0 else 0)) * value if current == 0 else current * value
                current = 0
            elif value == 100:
                current *= 100
            else:
                current += value
        return total + current

    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "":
            print("Please enter a number.")
            continue

        
        try:
            return int(user_input)
        except ValueError:
            pass

        
        try:
            
            words = user_input.replace("-", " ").split()
            return words_to_number(words)
        except ValueError:
            print("I didn't understand that number. Please enter a digit (like 12) or words (like twelve, twenty one, one hundred).")


def ask_yes_no(prompt):
    """Ask a yes/no question. Accepts y/yes/true/1, n/no/false/0."""
    while True:
        answer = input(prompt).strip().lower()
        if answer.startswith("y") or answer in {"true", "1"}:
            return True
        elif answer.startswith("n") or answer in {"false", "0"}:
            return False
        else:
            print("Please answer with 'yes' or 'no' (or just 'y' or 'n').")


def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 2
        print("✓ Good length (12+ characters)")
    elif len(password) >= 8:
        score += 1
        print("✓ Acceptable length (8+ characters)")
    else:
        print("✗ Too short (less than 8 characters)")

    if any(char in lowercase for char in password):
        score += 1
        print("✓ Contains lowercase letters")
    else:
        print("✗ No lowercase letters")

    if any(char in uppercase for char in password):
        score += 1
        print("✓ Contains uppercase letters")
    else:
        print("✗ No uppercase letters")

    if any(char in numbers for char in password):
        score += 1
        print("✓ Contains numbers")
    else:
        print("✗ No numbers")

    if any(char in symbols for char in password):
        score += 1
        print("✓ Contains symbols")
    else:
        print("✗ No symbols")

    print(f"\nStrength Score: {score}/6")
    if score >= 5:
        print("STRONG PASSWORD! 💪")
    elif score >= 3:
        print("MEDIUM PASSWORD - Could be better")
    else:
        print("WEAK PASSWORD - Please make it stronger!")

    return score


def generate_and_check_password(chosen_characters, num_passwords):
    password_length = parse_number("How long should each password be? ")
    results = []
    for i in range(num_passwords):
        password = ""
        for _ in range(password_length):
            password += random.choice(chosen_characters)

        print(f"\nGenerated Password #{i + 1}: {password}")
        print("\nChecking strength...")
        print("-" * 40)
        score = check_password_strength(password)
        results.append((password, score))
        print()
    return results


def save_to_file(results, filename):
    try:
        with open(filename, "w") as file:
            file.write("Generated Passwords Report\n")
            file.write("=" * 40 + "\n\n")
            for i, (pwd, score) in enumerate(results, start=1):
                file.write(f"Password #{i}: {pwd}\n")
                file.write(f"Strength Score: {score}/6\n")
                if score >= 5:
                    rating = "STRONG PASSWORD! 💪"
                elif score >= 3:
                    rating = "MEDIUM PASSWORD - Could be better"
                else:
                    rating = "WEAK PASSWORD - Please make it stronger!"
                file.write(f"Rating: {rating}\n")
                file.write("-" * 40 + "\n\n")
        abs_path = os.path.abspath(filename)
        print(f"Passwords saved successfully!")
        print(f"File location: {abs_path}")
    except Exception as e:
        print(f"Oops! Something went wrong while saving the file: {e}")


def main():
    
    print("=" * 60)
    print("  WELCOME TO THE BEST PASSWORD GENERATOR & STRENGTH CHECKER!")
    print("=" * 60)
    print(f"\nCurrent folder: {os.getcwd()}")
    print("(Any saved files will appear in this folder.)\n")

    
    while True:
        print("Which character types would you like to include? (y/n)")
        include_lower = ask_yes_no("Lowercase letters? ")
        include_upper = ask_yes_no("Uppercase letters? ")
        include_numbers = ask_yes_no("Numbers? ")
        include_symbols = ask_yes_no("Symbols? ")

        chosen_characters = ""
        if include_lower:
            chosen_characters += lowercase
        if include_upper:
            chosen_characters += uppercase
        if include_numbers:
            chosen_characters += numbers
        if include_symbols:
            chosen_characters += symbols

        if chosen_characters == "":
            print("Oops! You must select at least one character type. Let's try again.\n")
        else:
            break

    
    num_passwords = parse_number("How many passwords would you like to generate? ")

    
    results = generate_and_check_password(chosen_characters, num_passwords)

    
    save = ask_yes_no("Would you like to save these passwords to a file? (y/n): ")
    if save:
        filename = input("Enter a filename (e.g., passwords.txt): ")
        save_to_file(results, filename)
    else:
        print("Okay, not saving to file. Have a great day!")

if __name__ == "__main__":
    main()
