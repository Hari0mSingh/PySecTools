# Error Handling
# Libraries: Built-in try, except, finally

# Concepts: Catching exceptions, logging errors, ensuring clean-up actions.

num = int(input("Enter your age : "))

try:
    result = num/0
except ZeroDivisionError as e:
    print(f"Error has occured : {e}")

finally:
    print("Gracefully handled the error")
