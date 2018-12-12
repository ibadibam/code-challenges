from linkedLists import Node, LinkedList
def main():
	#create and populate test list	
	testList = LinkedList()
	for i in range(-10,10):
		testList.add(i)
	print(f'test list: {testList.toList()}')
	
	print(f'index of 5: {testList.indexOf(5)}')

	#negative test case should fail
	try:
		print(testList.indexOf('g'))
	except ValueError as e:
		print(e)

	#kthLast
	print("kthLast tests:")
	print (testList.kthLastNaive(0))
	print (testList.kthLast(0))
	print (testList.kthLastNaive(1))
	print (testList.kthLast(1))
	print (testList.kthLastNaive(2))
	print (testList.kthLast(2))

	#negative test cases should fail
	try:
		print (testList.kthLastNaive(1000))
	except OverflowError as e:
		print (e)
	try:
		print (testList.kthLast(1000))
	except OverflowError as e:
		print (e)

	#reverse
	print('reverse:')
	LinkedList.reverse(testList)
	print(testList.toList())

	#partition
	print('partition tests:')
	oddEven = lambda x : x % 2 == 0
	print(testList.partition(oddEven).toList())

	greaterLess = lambda x : x > 0
	print(testList.partition(greaterLess).toList())
	
if __name__ == "__main__": main()