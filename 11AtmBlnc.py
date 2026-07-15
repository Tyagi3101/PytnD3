correct_pin = 1234
account_balance = 5000.0

print("Welcome to the Python ATM Machine!")

entered_pin = int(input("Please enter your 4-digit PIN: "))

if entered_pin == correct_pin:
	print("\nPIN Verified Successfully!")
	print("1. Check Balance")
	print("2. Withdraw Cash")
    
	choice = int(input("Select an option (1 or 2): "))
    
	if choice == 1:
		print(f"\nYour current balance is: ${account_balance}")
        
	elif choice == 2:
		withdrawal_amount = float(input("\nEnter amount to withdraw: $"))
        
		if withdrawal_amount <= account_balance:
			account_balance -= withdrawal_amount
			print(f"Transaction successful! Please collect your cash.")
			print(f"Remaining balance: ${account_balance}")
		else:
			print("Transaction declined: Insufficient balance!")
            
	else:
		print("Invalid option selected!")
else:
	print("Access Denied: Incorrect PIN!")

print("\nThank you for using our ATM. Goodbye!")

