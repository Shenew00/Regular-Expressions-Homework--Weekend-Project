# import re
# with open("names.txt") as f:
#     data = f.read()
#     print(data)
  
#     firstname = (re.search(', (?P<first>[A-Z][a-z]+)',data)).group('first'), 
#     lastname = (re.search('[A-Z][a-z]+', data)).group()

#     print(firstname)
#     print(lastname)

# for person in data:
#     match = firstname.search(name)
#     match = lastname.search(name)

#     if match:
#         print('\n', f" {match.group(1)} {match.group(2)}")
  

# import re
# with open("regex_test.txt") as f:
#     data = f.readlines()
# print(data)

# pattern = re.compile("([A-Z][a-z]+)([A-Za-z]+)([A-Za-z])")

# for person in data:
#     match = pattern.search(person)

# if match:
#     print(f"{match.group()}")



import re
with open("names.txt") as f:
    data = f.readlines()
print(data)

pattern = re.compile("([A-Z][a-z]+) -([A-Z a-z]+)([A-Za-z])+") 

for person in data:
    match = pattern.search(person)

    if match:
        print(f"{match.group(1)}{match.group(2)}{match.group(3)}")