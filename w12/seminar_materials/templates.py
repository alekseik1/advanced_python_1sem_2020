import re

print(re.search(r'[0-9]{4}[abc]+[0-9]{3}', r'0123ccaabb275'))
print(re.findall(r'\ba[a-zA-Z]* ', 'I ate apple, drank juice meme'))

