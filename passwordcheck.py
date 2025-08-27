# Password Checker ~Manish Dey
# Checks if password contains at least 8 chars, uppercase, lowercase, digit, and special character
import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: password must be at least 8 characters long"
    
    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain an uppercase letter"
    
    if not any(char.islower() for char in password):
        return "Weak: password must contain a lowercase letter"
    
    if not re.search(r'[!@#$%^&*()_+\-={}\[\]:;"\'<>,.?/\\|]', password):
        return "Medium: password must contain a special character"
    
    return "Strong: password is secured!"

def password_checker():
    print("-> Welcome to the Password Strength Checker Tool")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool!")
            break
        
        result = check_password_strength(password)
        print(result)

# Run the tool
if __name__ == "__main__":
    password_checker()
