


f = open("/Users/benjaminbrooke/PycharmProjects/Python/Other Python Libraries/7.OS and Files/Names.txt")

print(f)
#<_io.TextIOWrapper name='/Users/benjaminbrooke/PycharmProjects/Python/Other Python Libraries/7.OS and Files/Names.txt' mode='r' encoding='UTF-8'>


print(f.read())
"""
Benjamin
Brooke
Harry
Brooke
Penny
Brooke
"""


f.close()







with open('filename.txt', 'r') as file:
    # Read or write to the file
    content = file.read()
    print(content)


file = open('filename.txt', 'r')

#The with statement automates this try-finally pattern.

try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensure the file is closed







