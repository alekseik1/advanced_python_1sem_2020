import re

print(re.findall(r'(a|b|c)\1', 'aabbc'))
# 0: a => (a|b|c) -> (a)
# 1: a: a = \1 === (a) - OK
# 1: 1 match, return to default state
# 2: b => (a|b|c) -> (b)
# 3: b: b = \1 === (b) - OK
# 3: another match, return to default state
# 4: c => (a|b|c) -> (c)
# 5: $: $ = \1 === (c) - NO
# 5: no match
# end of symbols, exiting

