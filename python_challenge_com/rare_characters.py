#!/usr/bin/python

from collections import Counter

import re

code = open("rare_characters.txt")

code_key = "#@!$%+{}[]_-&*()*^@/\n"
decoded_output =""

print()
for letter in code:
    if letter not in code_key:
        decoded_output += letter

decoded_output.strip()

print(decoded_output)

characters = Counter(code)
print(characters.most_common())

# message = re.findall("[a-zA-Z]", code)
# print message