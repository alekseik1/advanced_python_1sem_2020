import re

print(re.search('(ab){3}', 'ab aba abb ababab ab ab'))
print(re.findall('[ab]{3}', 'ab aba abb ababab ab ab'))


s = 'какой-то текст, <b>текст жирным шрифтом</b>, и снова какой-то текст'
m = re.search(r'<b>([\w\s]+)</b>', s)
print(m)
# m = re.findall(r'<b>([\w\s]+)</b>', s)
# print(m)
print(m.group(1))
print(m.groups())
