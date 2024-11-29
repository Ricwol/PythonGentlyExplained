"""Exercise #19: Password Generator

Write a `generatePassword()` function that has a `length` parameter.
The `length` parameter is an integer of how many characters the
generated password should have. For security reasons, if `length` is
less than 12, the function forcibly sets it to 12 characters anyway.
The password string returned by the function must have at least one
lowercase letter, one uppercase letter, one number, and one special
character.

The special characters for this exercise are `~!@#$%^&*()_+`.

Your solution should import Python's `random` module to help randomly
generate these passwords.
"""

def generatePassword(length: int) -> str:
    """Generate a password with a minimum length of 12."""
    return ''
