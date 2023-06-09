import re
import os

################################################################################

## Create a text file that has your full name, and write code to read it and
# extract first name, middle name and last name.
with open('name.txt','r') as file1:
    for file in file1:
        words = file.split(' ')

print('First name:',words[4])
print('Middle name:',words[5])
print('Last name:',words[3])
print('\n')
print('\n')

##################################################################################
# Using the library os, print your local file path on screen.
print('my local file path is:',os.getcwd)
print('\n')
print('\n')

###################################################################################
# Extraction of baby name from file using regex not using built-in libraries, 
# create a sort algorithm, implement binary search.

with open('baby2008.html','r') as file2:
	babyNames = re.findall(r'<td>([a-zA-Z]+)</td>', file2.read())

print("babies names are:",babyNames)
print('\n')

babyBoys,babyGirls = [],[]

for count,name in enumerate(babyNames):
	if count%2 == 0:
		babyBoys.append(name)
	else:
		babyGirls.append(name)

print("baby boys names are:",babyBoys)
print('\n')
print("baby girls names are:",babyGirls)
######################################################################################
