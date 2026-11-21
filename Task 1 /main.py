
# Task 1: Understand the Problem and Identify the Data
# Village Milk Co-operative Payment Calculator

# Constants
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Farmer details
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ")

# Calculate rate
fat_steps = round((fat - FAT_STANDARD) / 0.1)
snf_steps = round((snf - SNF_STANDARD) / 0.1)

rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)

# Calculate payment
amount = round(litres * rate, 2)

# Display results
print("\n--- Milk Payment Details ---")
print("Farmer ID:", farmer_id)
print("Quantity:", litres, "litres")
print("Fat:", fat, "%")
print("SNF:", snf, "%")
print("Shift:", shift)
print("Rate per litre: Rs.", round(rate, 2))
print("Total Payment: Rs.", amount)
