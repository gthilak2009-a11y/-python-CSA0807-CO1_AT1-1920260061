
# Task 11: Recommend and Defend the Final Design

from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
FAT_STANDARD = Decimal("3.5")
SNF_STANDARD = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")


# Function to calculate milk rate
def rate_per_litre(fat, snf):
    fat_steps = round((fat - FAT_STANDARD) / Decimal("0.1"))
    snf_steps = round((snf - SNF_STANDARD) / Decimal("0.1"))

    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)
    return rate.quantize(Decimal("0.01"))


# Function to calculate payment
def payout(litres, fat, snf):
    if litres <= 0:
        raise ValueError("Milk quantity must be positive")

    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat percentage")

    if not Decimal("5.0") <= snf <= Decimal("10.0"):
        raise ValueError("Invalid SNF percentage")

    rate = rate_per_litre(fat, snf)
    amount = litres * rate

    return amount.quantize(Decimal("0.01"))


# Main program
try:
    farmer_id = input("Enter Farmer ID: ")
    litres = Decimal(input("Enter milk quantity: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))

    rate = rate_per_litre(fat, snf)
    payment = payout(litres, fat, snf)

    print("\n--- Milk Payment Details ---")
    print("Farmer ID:", farmer_id)
    print("Milk Quantity:", litres)
    print("Fat Percentage:", fat)
    print("SNF Percentage:", snf)
    print("Rate per litre: Rs.", rate)
    print("Total Payment: Rs.", payment)

except Exception as e:
    print("Error:", e)
