

"""Convert two lists into a dictionary"""
from random import sample

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

list1 = zip(keys,values)
dict1 = zip(keys,values)

print(list(list1))
#[('Ten', 10), ('Twenty', 20), ('Thirty', 30)]

print(dict(dict1))
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


####################################################################

"""Merge two Python dictionaries into one"""

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)

print(dict1)
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

####################################################################


"""Print the value of key ‘history’ from the below"""

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict.values())
#dict_values([{'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}])

print(sampleDict.keys())
#dict_keys(['class'])

print(sampleDict['class']['student']['marks']['history'])
#80


####################################################################

"""In Python, we can initialize the keys with the same values."""

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

####################################################################

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

print(sample_dict['name'])
#Kelly


print(sample_dict.values())
#dict_values(['Kelly', 25, 8000, 'New york'])


for keys,values in sample_dict.items():
    print(keys,values)
#name Kelly
#age 25
#salary 8000
#city New york



res = dict()

for key,value in sample_dict.items():
    if 'name' in key:
        res.update({key:value})

print(res)
#{'name': 'Kelly'}

####################################################################

"""Delete a list of keys from a dictionary"""

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for k in keys:
    sample_dict.pop(k)
print(sample_dict)
#{'age': 25, 'city': 'New york'}

####################################################################

"""Python program to check if value 200 exists in the
 following dictionary."""

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
        print("true")
#true

####################################################################

Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')

print(sample_dict)

