
# Task 12: Re-evaluate and Adapt the Design

from decimal import Decimal

# Original and seasonal rate cards
BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

SUMMER_BASE_RATE = Decimal("32.00")
SUMMER_FAT_STEP_VALUE = Decimal("0.45")

BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")


# Function to calculate milk rate
def rate_per_litre(fat, snf, season):
    if season == "summer":
        base_rate = SUMMER_BASE_RATE
        fat_value = SUMMER_FAT_STEP_VALUE
    else:
        base_rate = BASE_RATE
        fat_value = FAT_STEP_VALUE

    fat_steps = round((fat - Decimal("3.5")) / Decimal("0.1"))
    snf_steps = round((snf - Decimal("8.5")) / Decimal("0.1"))

    rate = base_rate + (fat_steps * fat_value) + (snf_steps * SNF_STEP_VALUE)

    return rate.quantize(Decimal("0.01"))


# Function to calculate payment
def payout(litres, fat, snf, season):
    rate = rate_per_litre(fat, snf, season)
    return (litres * rate).quantize(Decimal("0.01"))


# Function to calculate bonus
def calculate_bonus(total_litres):
    if total_litres > BONUS_LIMIT:
        return (total_litres * BONUS_RATE).quantize(Decimal("0.01"))
    return Decimal("0.00")


# Main program
try:
    farmer_id = input("Enter Farmer ID: ")
    litres = Decimal(input("Enter milk quantity: "))
    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))
    season = input("Enter season (summer/normal): ").lower()

    if litres <= 0:
        raise ValueError("Quantity must be positive")

    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Invalid fat percentage")

    if not Decimal("5.0") <= snf <= Decimal("10.0"):
        raise ValueError("Invalid SNF percentage")

    if season not in ("summer", "normal"):
        raise ValueError("Invalid season")

    rate = rate_per_litre(fat, snf, season)
    payment = payout(litres, fat, snf, season)

    # Ten-day quantity and bonus
    total_litres = Decimal(input("Enter total ten-day litres: "))
    bonus = calculate_bonus(total_litres)

    print("\n--- Milk Payment Details ---")
    print("Farmer ID:", farmer_id)
    print("Season:", season)
    print("Milk Quantity:", litres)
    print("Fat:", fat)
    print("SNF:", snf)
    print("Rate per litre: Rs.", rate)
    print("Milk Payment: Rs.", payment)
    print("Ten-day Bonus: Rs.", bonus)
    print("Total Amount: Rs.", payment + bonus)

except ValueError as e:
    print("Invalid input:", e)
