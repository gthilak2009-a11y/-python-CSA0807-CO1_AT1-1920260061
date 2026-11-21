
# Task 10: Compare Expectations with Execution

from decimal import Decimal
import time

# Function to calculate float total
def total_float(payments):
    total = 0.0
    for amount in payments:
        total += float(amount)
    return total


# Function to calculate Decimal total
def total_decimal(payments):
    total = Decimal("0.00")
    for amount in payments:
        total += Decimal(amount)
    return total


# Test different payment sizes
sizes = [300, 6000, 150000]

for n in sizes:
    payments = ["33.40", "0.10"] * (n // 2)
    if n % 2:
        payments.append("33.40")

    # Measure float calculation time
    start = time.perf_counter()
    float_total = total_float(payments)
    float_time = time.perf_counter() - start

    # Measure Decimal calculation time
    start = time.perf_counter()
    decimal_total = total_decimal(payments)
    decimal_time = time.perf_counter() - start

    print("\nNumber of Payments:", n)
    print("Float Total:", round(float_total, 2))
    print("Decimal Total:", decimal_total)
    print("Difference:", abs(Decimal(str(float_total)) - decimal_total))
    print("Float Time:", float_time)
    print("Decimal Time:", decimal_time)


# Compare rounding methods
print("\n--- Rounding Comparison ---")

amounts = [Decimal("10.005"), Decimal("20.005")]

round_each = sum(
    (amount.quantize(Decimal("0.01")) for amount in amounts),
    Decimal("0.00")
)

round_total = sum(amounts).quantize(Decimal("0.01"))

print("Rounding Each Payment:", round_each)
print("Rounding Only Total:", round_total)


# Rate calculation using dictionary
print("\n--- Rate Table ---")

rate_table = {}

def get_rate(fat, snf):
    key = (fat, snf)

    if key not in rate_table:
        fat_steps = round((fat - 3.5) / 0.1)
        snf_steps = round((snf - 8.5) / 0.1)

        rate_table[key] = (
            30.00 + fat_steps * 0.40 + snf_steps * 0.30
        )

    return rate_table[key]


rate = get_rate(4.2, 8.7)

print("Milk Rate:", round(rate, 2))
print("Stored Rate Table:", rate_table)
