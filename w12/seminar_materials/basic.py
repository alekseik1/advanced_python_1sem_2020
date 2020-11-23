import re
s = [
    'с самого начала. у меня была , еее ся',
    'с самого начала. у меня была , войцв сь',
    'cnnn',
    'cccn',
    'cncncn',
]

expr = re.compile('^[cn]{3}')
res = [expr.search(i) for i in s]
print(res)

