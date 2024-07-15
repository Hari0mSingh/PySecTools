#  Security Best Practices
# Concepts: Writing secure code, understanding common vulnerabilities, input validation, sanitizing outputs.

import re
from html import escape

# Input validation
def validate_username(username):
    if re.match("^[a-zA-Z0-9_]+$", username):
        return True
    else:
        return False

# Example usage of validation
username = "valid_username_123"
if validate_username(username):
    print("Valid username")
else:
    print("Invalid username")

# Sanitizing output
user_input = "<script>alert('XSS')</script>"
safe_output = escape(user_input)
print(safe_output)

# Combining both
def process_username(username):
    if validate_username(username):
        print("Valid username:", escape(username))
    else:
        print("Invalid username")

# Example usage of combined process
process_username("valid_username_123")
process_username("invalid username<script>alert('XSS')</script>")
