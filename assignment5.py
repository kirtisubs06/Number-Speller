"""
Assignment 5: "Spelling Numbers"

Author: Kirti Subramanian
CWID: 20531478
Date: 10/30/2022

Program Description: This program takes in a number entered in integer form as the parameter
of the spell() function and returns the same number in spelled-out form (in words rather than
in digits).
"""


# Convert the one's place digit into a word.
def digit_name(digit):
    """
    Returns a string containing the English word naming "digit".
    "digit" must be between 1 and 9, inclusive
    """
    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""


# Convert the ten's place digit into a word if the number is a "teen" (between 10 and 19).
def teen_name(number):
    """
    Returns a string containing the English word naming "number".
    "number" must be between 10 and nineteen inclusive.
    """
    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""


# Convert the ten's place digit into a word.
def tens_name(number):
    """
    Returns a string containing the English word for just the tens part of
"number".
    "number" must be an integer between 20 and 99 inclusive.
    """
    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""


# Convert the hundred's place digit into a word.
def hundreds_name(number):
    """
    Returns a string containing the English word for just the hundreds part of
"number".
    "number" must be an integer between 100 and 999 inclusive.
    """
    if number >= 900: return "nine hundred"
    if number >= 800: return "eight hundred"
    if number >= 700: return "seven hundred"
    if number >= 600: return "six hundred"
    if number >= 500: return "five hundred"
    if number >= 400: return "four hundred"
    if number >= 300: return "three hundred"
    if number >= 200: return "two hundred"
    if number >= 100: return "one hundred"
    return ""


# Convert the number into words if the number is less than 1000.
def spell_number_less_than_thousand(number):
    """
    Returns a string containing the English words that spell out "number".
    "number" must be between 0 and 1000, exclusive.
    """
    part = number  # the part that still needs to be converted
    name = ""  # the name of the number
    if part >= 100:
        name = digit_name(part // 100) + " hundred"
        part = part % 100
    if part >= 20:
        name = name + " " + tens_name(part)
        part = part % 10
    elif part >= 10:
        name = name + " " + teen_name(part)
        part = 0
    if part > 0:
        name = name + " " + digit_name(part)
    return name


# This is the main function that will be called when a number is converted into a word.
def spell(number):
    """
        Returns a string containing the English words that spell out "number".
        "number" must be between -999999999 and 999999999, exclusive.
        """
    # Check if the number is negative or not.
    negative = False
    if number < 0:
        negative = True
        number = (-1 * number)

    part = number  # the part that still needs to be converted
    name = ""  # the name of the number
    position = 1

    if number == 0:
        name = "zero"
        return name

    if len(str(number)) == 3:
        spell_number_less_than_thousand(number)

    # special case
    digits = part % 100
    if 9 < digits < 20:
        name = teen_name(digits) + name
        part = part // 100
        position = 3

    while part > 0:
        # Check the 1st digit and add the respective word to the name string.
        if position == 1:
            digits = part % 10
            name = digit_name(digits) + " " + name
            part = part // 10
            position += 1
        # Check the 2nd digit and add the respective word to the name string.
        elif position == 2:
            digits = part % 10
            name = tens_name(digits * 10) + " " + name
            part = part // 10
            position += 1
        # Check the 3rd digit and add the respective word to the name string.
        elif position == 3:
            digits = part % 10
            name = hundreds_name(digits * 100) + " " + name
            part = part // 10
            position += 1
        # Check the 4th and 5th digits and add the respective words to the name string.
        elif position == 4:
            digits = part % 100
            if number % 1000000 != 0:
                if 9 < digits < 20:
                    name = teen_name(digits) + " thousand " + name
                else:
                    name = tens_name(digits) + " " + digit_name(digits % 10) + " thousand " + name
            part = part // 100
            position += 2
        # Check the 6th digit and add the respective word to the name string.
        elif position == 6:
            digits = part % 10
            name = hundreds_name(digits * 100) + " " + name
            part = part // 10
            position += 1
        # Check the 7th and 8th digits and add the respective words to the name string.
        elif position == 7:
            digits = part % 100
            if 9 < digits < 20:
                name = teen_name(digits) + " million " + name
            else:
                name = tens_name(digits) + " " + digit_name(digits % 10) + " million " + name
            part = part // 100
            position += 2
        # Check the 9th digit and add the respective word to the name string.
        elif position == 9:
            digits = part % 10
            name = hundreds_name(digits * 100) + " " + name
            part = part // 10

    # If the number is negative, prefix a "negative".
    if negative:
        name = "negative " + name
    return name


# Test the function.
print(spell(123456789))
print(spell(456678))
print(spell(66))
print(spell(-123456789))
print(spell(-456678) )
print(spell(-418))
print(spell(0))
print(spell(10234))

# Function Test Results.
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment5.py
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine 
four hundred fifty six thousand six hundred seventy eight 
sixty six 
negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine 
negative four hundred fifty six thousand six hundred seventy eight 
negative four hundred eighteen
zero
ten thousand two hundred thirty four 

Process finished with exit code 0
"""