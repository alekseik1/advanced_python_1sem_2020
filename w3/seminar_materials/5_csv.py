# CSV - comma separated values
'''
name;surname;father_name
Aleksei;Kozharin;Sergeevich
'''

import csv
with open('1.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        print(i)

with open('2.csv', 'a') as f:
    writer = csv.writer(f, delimiter=';')
    a = ['a', 'b', 'c']
    b = [['b', 'b', 'b'], ['a', 'a', 'a']]
    writer.writerow(a)
    writer.writerows(b)

