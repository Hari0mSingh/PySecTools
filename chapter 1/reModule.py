# Regular Expressions
# Libraries: re

# Concepts: Pattern matching, searching, extracting specific parts of strings.

import re

# Text to search
text = "I am Hariom and i am a Penetration tester having python scripting or automation skils."

# Search for the pattern 'rain' in the text
match = re.search(r'pytk', text)

# Check if a match was found
if match:
    print('Match found:', match.group())
else:
    print('No match found')


# o/p : Match found: python


