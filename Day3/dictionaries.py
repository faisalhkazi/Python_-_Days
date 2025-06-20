my_dictionary = {'c1': 'value1', 'c2': 'value2' }
print(my_dictionary)


result = my_dictionary['c1']
print(result)

customer = {'Name': 'Faisal', 'Last_Name': 'Kazi', 'Height': 5.10, 'Weight': 110}

name = customer['Name']
last_name = customer['Last_Name']
cust_height = customer['Height']
weight = customer['Weight']

print(f"The name of the customer is {name} {last_name} and have the height of {cust_height}feet and weight of {weight}KG")

print(f"The name of the customer is {customer['Name']} {last_name} and have the height of {cust_height}feet and weight of {weight}KG")

dic = {'k1': ['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}

dic['k3'] = ['g', 'h', 'i']         #THis is how you can add anything to the dictionary

print(dic)

print(dic['k2'][1].upper())

print(dic.values())         #To see only the values of the Key

print(dic.keys())           #To the only the Key inside the dictionary

