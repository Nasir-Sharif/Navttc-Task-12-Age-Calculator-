from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    
    # Check if birthday has occurred this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    return age

# Input for birthdate
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")

# Calculate age
age = calculate_age(birthdate)
print("Your age is:", age)
