import json

with open('1.json', 'r') as f:
    a = json.loads(f.read())
    # print(a)
    # print(type(a))
    f.seek(0)
    b = json.load(f)
    # print(b)
    # print(type(b))

a = {2: 'a', 3: [2, 3, 5]}
print(json.dumps(a))
with open('1_dump.json', 'w') as fp:
    json.dump(a, fp)

