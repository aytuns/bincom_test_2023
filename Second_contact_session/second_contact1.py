## Create a text file that has your full name, and write code to read it and
# extract first name, middle name and last name.
with open('name.txt','r') as file1:
    for file in file1:
        words = file.split(' ')

print('First name:',words[4])
print('Middle name:',words[5])
print('Last name:',words[3])
