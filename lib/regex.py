import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab

# Name regex to match proper names (e.g., "John Cena", "Anya Taylor-Joy", "D'Angelo")
name = r"^[A-Z][a-zA-Z]*([ '-][A-Z][a-zA-Z]*)*$"
name_regex = re.compile(name)

# Phone regex to match phone numbers in various formats
phone_number = r"^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email regex to match valid email addresses (no numbers at the start)
email_address = r"^[A-Za-z][A-Za-z0-9]*(?:[.-_][A-Za-z0-9]+)*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)

