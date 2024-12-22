import re


def find_emails(text):
    email_pattern = r'[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, text)

    for email in emails:
        print(email)


sample_text = """
    Please contact us at support@example.com, sales.company@corporation.net, or feedback@sample.co.uk.
    Incorrect emails like @example.com, john.doe@.com, or john@doe. are not valid and should NOT be captured.
"""

find_emails(sample_text)