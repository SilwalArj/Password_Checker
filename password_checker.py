import string
from getpass import getpass

def has_lower(pwd):
    return any(char in string.ascii_lowercase for char in pwd)

def has_upper(pwd):
    return any(char in string.ascii_uppercase for char in pwd)

def has_special(pwd):
    return any(char in string.punctuation for char in pwd)

def has_digits(pwd):
    return any(char in string.digits for char in pwd)

def main():
    while True:
        pwd = getpass("Enter your password: ")

        if pwd == "exit":
            print("Exiting pwchecker")
            break

        lower_ok = has_lower(pwd)
        upper_ok = has_upper(pwd)
        special_ok = has_special(pwd)
        digits_ok = has_digits(pwd)

        score = 0

        if len(pwd) >=12:
            score +=3
        elif len(pwd) >=8:
            score +=2

        if lower_ok:
            score +=1

        if upper_ok:
            score +=1
        
        if special_ok:
            score +=1
        
        if digits_ok:
            score +=1
        
        if score >=5:
            print("Password is strong!")
        
        elif score >=3:
            print("Password is moderate!")
        
        else:
            print("Password is weak!")
        
        print(f"Password score:{score}/7")

        if not lower_ok:
            print("Missing a lowercase letter!")
        
        if not special_ok:
            print("Missing a special character!")
        
        if not upper_ok:
            print("Missing a uppercase letter!")
        
        if not digits_ok:
            print("Missing a digit!")
        
        if len(pwd) < 8:
            print("Password length is under 8 characters!")

if __name__ =="__main__":
    main()