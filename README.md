# Spelling Numbers

## Overview
This Python program is designed to convert numbers from their integer form to a spelled-out form in English. It can handle both positive and negative integers within a specified range.

### Author
- **Author:** Kirti Subramanian
- **CWID:** 20531478
- **Date:** 10/30/2022

## Description
The program includes a function `spell(number)` that takes an integer as input and returns its corresponding English word representation. The function supports numbers from -999,999,999 to 999,999,999 (exclusive). It handles individual digits, teens, tens, hundreds, thousands, and millions.

## Features
- **Digit to Word Conversion:** Converts individual digits to their corresponding English words.
- **Handling Teen Numbers:** Special handling for numbers between 10 and 19.
- **Tens and Hundreds Conversion:** Converts tens and hundreds place values to words.
- **Large Numbers:** Supports spelling out numbers up to the millions.
- **Negative Numbers:** Capable of handling negative numbers by prefixing with 'negative'.

## Usage
### Running the Program
To use the program, call the `spell()` function with an integer as the argument.

### Example Interaction
```python
print(spell(123456789))
print(spell(-418))
print(spell(0))
print(spell(10234))

# Output:
# one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine 
# negative four hundred eighteen
# zero
# ten thousand two hundred thirty four 

# Process finished with exit code 0
