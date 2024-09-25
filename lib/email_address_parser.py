# Write a program that takes in a string of email addresses, and parses the string into an array.
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses
    def parse(self):
        emails = re.split(r'[\s,]+', self.email_addresses)

        email_pattern= r'[\w\.-]+@[\.\w]'

        valid_emails = {email for email in emails if re.match(email_pattern, email)}

        return sorted(valid_emails)
        
