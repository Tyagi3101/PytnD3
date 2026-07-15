# 1. Inputs & Slab Boundaries
units = int(input("Enter the number of units consumed: "))
fixed_charge = 150.0  # ₹150 base fixed charge

slab1_limit, slab1_rate = 100, 3.00 # First 100 units at ₹3.00
slab2_limit, slab2_rate = 200, 4.50 # Next 100 units at ₹4.50
slab3_rate = 6.50                   # Remaining units at ₹6.50

# 2. Slab Calculation
s1 = min(units, slab1_limit) * slab1_rate
s2 = max(0, min(units - slab1_limit, slab2_limit - slab1_limit)) * slab2_rate
s3 = max(0, units - slab2_limit) * slab3_rate

# 3. Totals
energy_charge = s1 + s2 + s3
total_bill = energy_charge + fixed_charge

print("Energy Charges:", s1, "+", s2, "+", s3, "=", energy_charge)
print("Total Bill Amount:", total_bill)
