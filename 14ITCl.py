
""" def main():
	try:
		income = float(input("Enter your taxable income (in Rs.): "))
	except ValueError:
		print("Invalid input. Please enter a numeric value.")
		return """


income = float(input("Enter your taxable income (in Rs.): "))

tax = 0.0

if income <= 400000:
	tax = 0
elif income <= 800000:
	tax = (income - 400000) * 0.05
elif income <= 1200000:
	tax = (400000 * 0.05) + (income - 800000) * 0.10
elif income <= 1600000:
	tax = (400000 * 0.05) + (400000 * 0.10) + (income - 1200000) * 0.15
elif income <= 2000000:
	tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (income - 1600000) * 0.20
elif income <= 2400000:
	tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (income - 2000000) * 0.25
else:
	tax = (400000 * 0.05) + (400000 * 0.10) + (400000 * 0.15) + (400000 * 0.20) + (400000 * 0.25) + (income - 2400000) * 0.30

cess = tax * 0.04
total_tax_liability = tax + cess

print(f"Base Income Tax: Rs. {tax:.2f}")
print(f"Health & Education Cess (4%): Rs. {cess:.2f}")
print(f"Total Tax Liability: Rs. {total_tax_liability:.2f}")


""" if __name__ == '__main__':
	main() """
