# Navttc-Task-12-Age-Calculator-

# Age Calculator

## Description

This Python script calculates the age of a person based on their birthdate. The script asks for the user's birthdate in the format `YYYY-MM-DD` and then calculates the age by comparing the birthdate with the current date.

## Code

```python
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
```

## Steps

1. **Import Required Module:**
   - Import the `datetime` module, which is used to work with dates and times.

2. **Define the `calculate_age` Function:**
   - This function takes the user's birthdate as input and calculates their age by comparing it with the current date.
   - It also checks whether the user's birthday has occurred this year, adjusting the age accordingly.

3. **Get User's Birthdate:**
   - Prompt the user to input their birthdate in the `YYYY-MM-DD` format.

4. **Convert the Input to a Date Object:**
   - Convert the input string into a `datetime` object using `strptime`.

5. **Calculate and Print the Age:**
   - Call the `calculate_age` function to compute the age and print the result.

## How to Run

1. **Ensure Python is Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script:**
   - Save the provided Python code into a file named `12-Age Calculator (Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `12-Age Calculator (Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 12-Age Calculator (Nasir Sharif).py
     ```

4. **Enter Birthdate:**
   - Input your birthdate in the format `YYYY-MM-DD` when prompted.

5. **View Output:**
   - The script will display your age based on the provided birthdate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
