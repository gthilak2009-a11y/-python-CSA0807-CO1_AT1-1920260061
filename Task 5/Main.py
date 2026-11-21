
# Task 5: Read Input and Convert Types

# Get farmer details
farmer_id = input("Enter Farmer ID: ")

try:
    litres = float(input("Enter milk quantity in litres: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))

    shift = input("Enter shift (Morning/Evening): ")

    # Validate input
    if litres <= 0:
        print("Invalid quantity")
    elif not (2.0 <= fat <= 7.0):
        print("Invalid fat percentage")
    elif not (5.0 <= snf <= 10.0):
        print("Invalid SNF percentage")
    else:
        print("\n--- Farmer Details ---")
        print("Farmer ID:", farmer_id)
        print("Quantity:", litres, "litres")
        print("Fat:", fat, "%")
        print("SNF:", snf, "%")
        print("Shift:", shift)
        print(f"Quantity: {litres:8.2f}")
        
except ValueError:
    print("Invalid input! Please enter numbers only.")
