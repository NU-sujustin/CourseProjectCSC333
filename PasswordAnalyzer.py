import string

#define a function to ask to enter password
#strength of password will start at 0
#all counts of lower, numbers, whitespace, and special counts will be at 0
def check_password():
    password = input("Enter Password: ")
    strength = 0
    lower_count = upper_count = num_count = whitespace_count = special_count = 0

#Check how strong the user's password is then give feedback to user
    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1
    if len(password) >= 8:
        strength += 1

#if password doesn't meet specific requirements
#print to let user know what they are missing
    if len(password) < 8:
        remarks = "Password is too short! Must be at least 8 characters long."
    elif whitespace_count > 0:
        remarks = "Please do not use spaces in your password"
    elif strength < 5:
        remarks = "Password doesn't meet requirements. Try including upper, lower, numbers, special characters, and avoid using spaces."
    else:
        remarks = "Password meets requirements!"

#print number of lower, upper, number, special, whitespace count, and character count
    print("\nYour password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{special_count} special characters")
    print(f"{whitespace_count} whitespace characters")
    print(f"{len(password)} out of 8 characters")

#print password strength 1-5/5
    print(f"\nPassword Strength: {strength}/5")
    print(f"Hint: {remarks}\n")

#prompt if user decides to say yes and check for password
#if no ends program
def ask_password(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print('Invalid input. Please enter "yes" or "no".')

#Greet user and ask if they want to use password analyzer.
#loop if user says yes on checking another password
if __name__ == '__main__':
    print('Welcome to Password Analyzer!\n')
    if ask_password("Do you want to check a password strength? (yes/no): "):
        while True:
            check_password()
            if not ask_password("Do you want to enter another password? (yes/no): "):
                print("Thank You for using Password Analyzer!")
                break
    else:
        print("Thank You for using the Password Analyzer!")