import re

def validate_email(email):
    """
    Validates an email address using a regular expression.
    Returns True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Example usage ok
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_email.py <email>")
        sys.exit(1)

    input_email = sys.argv[1]
    if validate_email(input_email):
        print(f"{input_email} is a valid email address.")
    else:
        print(f"{input_email} is not a valid email address.")