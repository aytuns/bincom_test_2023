from bs4 import BeautifulSoup
import psycopg2
from random import randint


#Fetch the html file
html_page =  open('python_class_question.html', 'r')
#Parse the HTML file with beautifulsoup
soup = BeautifulSoup(html_page, 'html.parser')

"""
QUESTIONS TO BE ANSWERED
1.      Which color of shirt is the mean color?
2.      Which color is mostly worn throughout the week?
3.      Which color is the median?
4.      BONUS Get the variance of the colors
5.      BONUS if a colour is chosen at random, what is the probability that the color is red?
6.      Save the colours and their frequencies in postgresql database
7.      BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
8.      Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
9.      Write a program to sum the first 50 fibonacci sequence.
"""

color = soup.find_all('td')
colorlist1 = list()
colorlist2 = list()

# Put the required 'td' in a list
for count,col in enumerate(color):
	if (count % 2 != 0):
		colorlist1.append(col.text.replace(" ",""))
# Parse to a string to combine all the lists items
str1 = ''.join(colorlist1)
# Convert the string back to a list
colorlist2 = str1.split(',')

# Itemize the colors by frequencies into a dictionary
color_dict= dict()
for col in colorlist2:
	color_dict[col] = color_dict.get(col,0) +1

#Get the total number of colors worn for the week
sum1 = 0
for key,value in color_dict.items():
	sum1 +=value
total_color_num = sum1


bigcount = 0
bigcolor = ''
for key,val in color_dict.items():
    if (val > bigcount):
        bigcolor = key
        bigcount = val

##########################################################################################
# Which color of shirt is the mean color?
mean = total_color_num / len(colorlist1)
if mean < bigcount:
	print(f"The mean color is: {bigcolor} with mean value of: {mean}")

# Which color is mostly worn throughout the week?
print(f"The color mostly worn is: {bigcolor} with a frequency of: {bigcount}")

# Which color is the median?
median = total_color_num//2
colorlist2.sort()
print(f"The median color is {colorlist2[median]} with a median vaule of {median}")

# BONUS if a colour is chosen at random, what is the probability that the color is red?
prob_of_red = color_dict['RED'] / total_color_num
print(f"The probability of choosing red at random in {prob_of_red:.3f}")
print('\n')

############################################################################
# Save the colours and their frequencies in postgresql database
try:
	#CONNECT TO ALREADY CREATED DATABASE CALLED bincom_test
	conn = psycopg2.connect(
		database = 'postgres',
		user = 'postgres',
		password = 'password'
	)
	conn.autocommit = True
	cursor = conn.cursor()

	# CREATE A TABLE CALLED weekly_color
	sql_create_table = '''CREATE TABLE weekly_color
	(color_num int NOT NULL,
	colors varchar(10),
	frequencies int);
	'''
	cursor.execute(sql_create_table)

	# INSERT COLOR DATA INTO THE TABLE
	columnid = [(i+1) for i in range(len(color_dict))]
	columns = [(key,value) for (key,value) in color_dict.items()]

	for enum,values in enumerate(columns):
		cursor.execute('''INSERT INTO weekly_color
			(color_num,colors,frequencies) VALUES(%(int)s,%(str)s,%(int)s)''',(columnid[enum],values))
	conn.commit()

	cursor.execute('''SELECT * FROM weekly_color''')

	for i in cursor.fetchall():
		print("color_num",i[0])
		print("colors = ",i[1])
		print("frequency = ", i[2])
		print('\n')

except Exception as e:
	print('Error in DB: ',e)
	print('\n')

#################################################################################
# BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def find_number(x):
	if x == None:
		try:
			x = int(input('type a number between 1-100: '))
		except:
			print('please input an integer')
	list = [i for i in range(101)]
	if x in list:
		print(f"Your number {x} is present in the range of: ", (len(list)-1))
		print('\n')
	else:
		return(find_number(None))

find_number(100)

###################################################################################
# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

strand = ""
for i in range(4):
    rand1 = randint(0,1)
    strand += str(rand1)
print("The generate binary is: ",strand)
print("The Decimal equivalent is: ", int(strand,2))
print('\n')

##################################################################################
# Write a program to sum the first 50 fibonacci sequence.

n0, n1 = 0, 1
fib = [n0,n1]
for i in range(2,50):
	n2 = n0 + n1
	n0 = n1
	n1 = n2
	fib.append(n2)
print('the fibonacci list for the first 50 numbers is: ', fib)
print('The sum of this fibonacci list is: ',sum(fib))
print('\n')