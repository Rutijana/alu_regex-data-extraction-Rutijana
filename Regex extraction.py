import re

# Sample text containing various data types
text = """
Contact us at user@example.com or visit https://www.example.com.
Call us at (123) 456-7890 or 123-456-7890.
Your credit card number is 1234-5678-9012-3456.
The meeting is at 2:30 PM or 14:30.
Here are some HTML tags: <p>Hello</p> <div>World</div>.
Follow us on #example and #ThisIsAHashtag.
Prices start at $19.99 and can go up to $1,234.56.
"""

# Regular expressions for different data types
patterns = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?://[^\s/$.?#].[^\s]*",
    "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit_cards": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
    "time": r"(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AP]M)?",
    "html_tags": r"<[^>]+>",
    "hashtags": r"#\w+",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Extracting and printing data
for name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{name}: {matches}")