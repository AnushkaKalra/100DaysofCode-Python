"""
Global scope can be incredibly useful, especially when you're defining constants.
Global constants are variables which you define, and you're never planning on changing it ever again.
Their job is meant to be "set and forget" so you can use their values but never need to modify them.
"""

# Global constants are normally declared in ALL_CAPS with an underscore in between.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"

print(f"Value of pi is: {PI}")
print(f"URL for Google is: {GOOGLE_URL}")