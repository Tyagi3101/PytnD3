number = int(input("Enter a number: "))
if number > 0:
    print("Number is Positive")
elif number < 0:
    print("Number is Negative")
else:
    print("Number is Zero")



#PRACTICE NOTES

""" password = "Python123"

if password == "Python123":
    print("Login Successful")
else:
    print("Wrong Password") """


""" balance = 5000

pin = 1234

if pin == 1234:
    if balance >= 1000:
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")
else:
    print("Wrong PIN") """


""" Ternary Operator
print("Adult" if age >= 18 else "Minor")

status = "Adult" if age >= 18 else "Minor"
print(status)"""


#Logical Operators
#and, or, not
""" age = 25

salary = 50000

if age >= 18 and salary >= 30000:
    print("Loan Approved") """


""" marks = 35

sports = True

if marks >= 40 or sports:
    print("Admission Granted") """


""" logged_in = False

if not logged_in:
    print("Please Login") """


""" Truthy and Falsy Values
Python treats some values as False automatically.

Falsy values:

0	0.0	''	[]	{}	set()	None	False """

#Everything else is considered True.

""" name = ""

if name:
    print("Name exists")
else:
    print("Empty") """


""" if age == 18:

age = input("Age: ")
if age >= 18:
This causes an error because input() returns a string. """


#ATM
""" balance = 10000
amount = 2500

if amount <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance") """


#Login
""" username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials") """


