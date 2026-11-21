
# Task 9: Implement and Test the Calculator

# Constants
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


# Function to calculate rate
def rate_per_litre(fat, snf):
    fat_steps = round((fat - FAT_STANDARD) / 0.1)
    snf_steps = round((snf - SNF_STANDARD) / 0.1)

    return round(BASE_RATE + (fat_steps * FAT_STEP_VALUE)
                 + (snf_steps * SNF_STEP_VALUE), 2)


# Function to calculate payment
def payout(litres, fat, snf):
    if litres <= 0:
        raise ValueError("Quantity must be positive")
    if not 2.0 <= fat <= 7.0:
        raise ValueError("Invalid fat percentage")
    if not 5.0 <= snf <= 10.0:
        raise ValueError("Invalid SNF percentage")

    return round(litres * rate_per_litre(fat, snf), 2)


# Test cases
def test_calculator():
    assert payout(10, 3.5, 8.5) == 300.00
    assert payout(10, 4.2, 8.7) == 334.00
    assert payout(12, 3.1, 8.3) == 333.60
    assert payout(10, 2.0, 8.5) == 240.00
    assert payout(10, 7.0, 8.5) == 440.00

    print("All test cases passed successfully!")


# Main program
test_calculator()

print("\n--- Milk Payment Calculator ---")

try:
    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter milk quantity: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    amount = payout(litres, fat, snf)

    print("\nFarmer ID:", farmer_id)
    print("Rate per litre: Rs.", rate_per_litre(fat, snf))
    print("Total Payment: Rs.", amount)

except ValueError as e:
    print("Invalid input:", e)
