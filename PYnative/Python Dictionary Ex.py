

"""Convert two lists into a dictionary"""

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

