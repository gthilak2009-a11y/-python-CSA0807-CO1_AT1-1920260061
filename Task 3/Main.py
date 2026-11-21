
# Task 3: Choose Variables and Name the Constants

# Define constants
BASE_RATE = 30.00
FAT_RATE = 0.40
SNF_RATE = 0.30
FAT_STANDARD = 3.5
SNF_STANDARD = 8.5

# Farmer details
farmer_id = "F101"
litres = 10
fat = 4.2
snf = 8.7

# Calculate fat and SNF steps
fat_steps = round((fat - FAT_STANDARD) / 0.1)
snf_steps = round((snf - SNF_STANDARD) / 0.1)

# Calculate milk rate
rate = BASE_RATE + (fat_steps * FAT_RATE) + (snf_steps * SNF_RATE)

# Calculate total payment
amount = round(litres * rate, 2)

# Display results
print("Farmer ID:", farmer_id)
print("Milk Quantity:", litres)
print("Fat Percentage:", fat)
print("SNF Percentage:", snf)
print("Rate per Litre:", rate)
print("Total Payment:", amount)

# Multiple assignment and swapping
a, b = 10, 20
a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)
