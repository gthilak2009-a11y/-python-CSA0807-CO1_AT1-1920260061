
# Task 4: Write Correct Expressions

# Constants
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Input values
litres = 10
fat = 4.2
snf = 8.7

# Calculate fat and SNF steps
fat_steps = round((fat - FAT_STANDARD) / 0.1)
snf_steps = round((snf - SNF_STANDARD) / 0.1)

# Calculate rate per litre
rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)

# Calculate total amount
amount = round(litres * rate, 2)

# Display results
print("Fat Steps:", fat_steps)
print("SNF Steps:", snf_steps)
print("Rate per Litre: Rs.", round(rate, 2))
print("Total Amount: Rs.", amount)

# Demonstrate expressions
print("\nExpression Examples:")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("round(2.675, 2) =", round(2.675, 2))

# Check valid fat range
print("\nFat is valid:", 2.0 <= fat <= 7.0)
