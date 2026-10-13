# question no 1
try:
    n1 = int(input("enter first : "))
    n2 = int(input("enter second : "))
    result = n1/n2
    print(f"Result : {result}")
except ZeroDivisionError as e:
    print("Error : cannot divde by zero")


# question no 2

try:
    user = input("enter the no. ")
    no = int(user)
    result = 100/no
    print(f"100 divided by {no} is {result}")

except ValueError as e :
    print("error : enter the valid integer")

except ZeroDivisionError as e:
    print("Error : cannot divde by zero")


# question no 3

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("Number cannot be negative.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:   # when no exception are there
    print(f"Success! You entered: {number}")
finally:  # runs all time
    print("Execution complete. Cleaning up resources...\n")


# question no 4

user_profile = {"username": "alex123", "role": "admin"}

try:
    # Trying to access a dictionary key that doesn't exist
    print(user_profile["email"])
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Program continues smoothly after catching the error.")



# question no 5
def withdraw_money(balance, amount):
    if amount > balance:
        raise ValueError(f"Insufficient funds! Your balance is ${balance:.2f}.")
    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")
    
    return balance - amount

# Testing the function with exception handling
account_balance = 100.00

try:
    # Trying to withdraw more than we have
    new_balance = withdraw_money(account_balance, 150.00)
    print(f"Withdrawal successful. Remaining balance: ${new_balance:.2f}")
except ValueError as error:
    print(f"Transaction failed: {error}")
