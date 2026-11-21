
# Task 6: Organise the Logic into Functions

# Constants
BASE_RATE = 30.00
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - FAT_STANDARD) / 0.1)
    snf_steps = round((snf - SNF_STANDARD) / 0.1)

    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the total payment."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


def ten_day_total(payments):
    """Calculate the total payment for ten days."""
    total = 0
    for amount in payments:
        total += amount
    return round(total, 2)


# Main program
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

payments = [amount, 300.00, 250.00]
total = ten_day_total(payments)

print("\n--- Milk Payment Details ---")
print("Farmer ID:", farmer_id)
print("Rate per litre: Rs.", rate)
print("Payment: Rs.", amount)
print("Ten-day total: Rs.", total)
