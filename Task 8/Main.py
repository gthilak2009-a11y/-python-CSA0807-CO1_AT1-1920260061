
# Task 8: Plan the Algorithm Before Coding

# Constants
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

# Function to calculate milk rate
def rate_per_litre(fat, snf):
    fat_steps = round((fat - FAT_STANDARD) / 0.1)
    snf_steps = round((snf - SNF_STANDARD) / 0.1)

    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)
    return round(rate, 2)


# Function to calculate payment
def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


# Main program
n = int(input("Enter number of entries: "))
total = 0.0

for i in range(n):
    print("\nEntry", i + 1)

    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter milk quantity: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    # Validate input
    if litres <= 0 or not (2.0 <= fat <= 7.0) or not (5.0 <= snf <= 10.0):
        print("Invalid entry. Please enter valid values.")
        continue

    rate = rate_per_litre(fat, snf)
    amount = payout(litres, fat, snf)

    total += amount

    print("Farmer ID:", farmer_id)
    print("Rate per litre: Rs.", rate)
    print("Payment: Rs.", amount)

print("\nTen-Day Total Payment: Rs.", round(total, 2))
