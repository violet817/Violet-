# ---------------- Age Calculator ----------------
from datetime import datetime

# Constant (current year from system)
CURRENT_YEAR = datetime.now().year

# Ask the user for their birth year (variable)
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = CURRENT_YEAR - birth_year

# Display result
print("You are", age, "years old in", CURRENT_YEAR)
