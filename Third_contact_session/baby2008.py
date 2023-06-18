import re

# Extraction of baby name from file using regex not using built-in libraries, 
# create a sort algorithm, implement binary search.

with open('baby2008.html','r') as file2:
	babyNames = re.findall(r'<td>([a-zA-Z]+)</td>', file2.read())

babyBoys,babyGirls = [],[]

for count,name in enumerate(babyNames):
	if count%2 == 0:
		babyBoys.append(name)
	else:
		babyGirls.append(name)

