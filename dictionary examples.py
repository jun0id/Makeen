dic = {1:"a", 2:'d'}
print(dic.get(5,'f'))

print('-------------------------')
dic = {1:"a", 2:'d'}
for x in dic:
    print(dic)

print('-------------------------')

dic = {1:"a", 2:'d'}
for x in dic:
    print(dic[x])

print('-------------------------')

dic = {1:"a", 2:'d'}
for x in dic:
    print(dic.values())
    
print('-------------------------')

dic = {1:{"name": "ali", "age": 23},
       2:{"name": "aa", "age": 30}}

for key in dic:
    print(dic[key]['name'])
    
print('-------------------------')

dic = {1:{"name": "ali", "age":23},
       2:{"name": "aa", "age":30}}

for key in dic:
    for key1 in dic[key]:
        print(dic[key][key1])

print('-------------------------')

dec= {1:{'name':'John', 'age': 27, 'sex':'Male'},
    2:{'name':'Maria', 'age': 22, 'sex':'Female'},
    3:{'name':'Sali', 'age': 23, 'sex':'Female'}}

for key in dec:
    if (dec[key]['age'] > 22):
        print(dec[key])

print('-------------------------')

dec= {1:{'name':'John', 'age': 27, 'sex':'Male'},
    2:{'name':'Maria', 'age': 22, 'sex':'Female'},
    3:{'name':'Sali', 'age': 23, 'sex':'Female'}}

for key in dec:
    if (dec[key]['sex'] == 'Female' ):
        print(dec[key])

print('-------------------------')

dec= {1:{'name':'John', 'age': 27, 'sex':'Male'},
    2:{'name':'Maria', 'age': 22, 'sex':'Female'},
    3:{'name':'Sali', 'age': 23, 'sex':'Female'}}

for key in dec:
    if (dec[key]['age'] > 22):
        print(dec[key]['name'])

print('-------------------------')

dec= {1:{'name':'John', 'age': 27, 'sex':'Male'},
    2:{'name':'Maria', 'age': 22, 'sex':'Female'},
    3:{'name':'Sali', 'age': 23, 'sex':'Female'}}

for key in dec:
    if (dec[key]['age'] > 22):
        print(dec[key]['age'])
        

