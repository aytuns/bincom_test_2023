## Implement a Fibonacci series generator.

def fibSeries():
	numCount = int(input("enter number of fib series to be generated: "))
	fibList = [0,1]
	count = 2

	if numCount <= 1:
		fibList = [0]
		print('fibnonacci series is:',fibList)
	elif numCount == 2:
		print('fibnonacci series is:',fibList)
	elif numCount > 3:
		while count < numCount:
			fibList.append(fibList[count-2]+fibList[count-1])
			count += 1
		print('fibnonacci series is:',fibList)

fibSeries()