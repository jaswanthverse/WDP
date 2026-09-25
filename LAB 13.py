# sams_json_regex.py
import json
import re
from datetime import datetime

# Regex patterns
EMAIL_PATTERN = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
PHONE_PATTERN = r'^[6-9][0-9]{9}$'
ROLL_PATTERN = r'^SAMS\d{2}[A-Z]{2}\d{3}$'

# Sample JSON data
sample_json = '''
[
  {"name": "Ananya Rao", "roll_no": "SAMS24CS014", "email": "ananya.rao@edutech.edu", "phone": "9876543210"},
  {"name": "Zoya Khan", "roll_no": "SAMS24CS099", "email": "bad-email", "phone": "12345"}
]
'''

def parse_admissions(json_text):
    """Parse JSON string into Python objects."""
    return json.loads(json_text)

def validate_record(record):
    """Validate a single student record using regex patterns."""
    roll_no = record