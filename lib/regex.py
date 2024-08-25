import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

# Regular expression for names
# Matches names with uppercase and lowercase letters, optionally including hyphens or apostrophes, and at least one space between words
name_regex = re.compile(r"^[A-Z][a-z]*(?: [A-Z][a-z]*|\-[A-Z][a-z]*|\'[A-Z][a-z]*)+$")

# Regular expression for phone numbers
# Matches 10-digit numbers, formatted with optional hyphens or enclosed in parentheses and followed by a space
phone_regex = re.compile(r"^(?:\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{10})$")

# Regular expression for email addresses
# Matches emails with alphanumeric characters and dots in the local part, followed by an @ symbol and a domain name
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*([.][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.][a-zA-Z]{2,})+$")
