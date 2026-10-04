import re
phone_pattern = r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})'

text = "Call me at 555-123-4567 or (555) 123-4567 or 555.123.4567"
phone_numbers = re.findall(phone_pattern, text)

normalized_numbers = [f"{area}-{prefix}-{line}" for area, prefix, line in phone_numbers]
print("Extracted and normalized phone numbers:", normalized_numbers)