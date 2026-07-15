age = int(input("Enter your age: "))
salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score (300-850): "))

if age < 21 or age > 65:
    print("\nLoan Rejected")
    print("Age must be between 21 and 65 years.")

elif salary < 60000:
    print("\nLoan Rejected")
    print("Minimum monthly salary requirement must be Rs. 60,000.")

elif credit_score < 760:
    print("\nLoan Rejected")
    print("Credit score is too low. Minimum required is 760.")

else:
    print("\nCongratulations! Loan Approved!")
