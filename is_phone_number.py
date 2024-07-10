import re

# Rigid way of validating phone number
"""  
def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
        
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
"""

def is_phone_number(text):
    phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")


def find_phone_number(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if is_phone_number(chunk):
            print(f"phone number found: {chunk}")

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
find_phone_number(message)