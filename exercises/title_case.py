"""Exercise #35: Title Case

Write a `getTitleCase()` function with a `text` parameter.
The function should return the title case form of the string. Every
word begins with an uppercase and the remaining letters are lowercase.
Non-letter characters separate words in the string. This means that
`'Hello World'` is considered to be two words while `'HelloWorld'` is
considered to be one word. Not only spaces, but all non-letter characters
can separate words, so `'Hello5World'` and `'Hello@World'` also have two words.

Python's `upper()` and `lower()` string methods return uppercase and
lowercase forms of the string, and you can use these in your implementation.
You may also use the `isalpha()` string method, which returns True if
the string contains only uppercase or lowercase letter characters.

However, you may not use Python's `title()` string method, as that would
defeat the purpose of the exercise.

Similarly, while you need to split up a string into individual words,
don't use Python's `split()` string method.
"""

def getTitleCase(text: str) -> str:
    """Return the title case form of `text`."""
    return ''
