dec= {1:{'name':'John', 'age': 27, 'sex':'Male'},
    2:{'name':'Maria', 'age': 22, 'sex':'Female'},
    3:{'name':'Sali', 'age': 23, 'sex':'Female'}}

for key in dec:
    if (dec[key]['age'] > 22):
        print(dec[key]['name'])
        

