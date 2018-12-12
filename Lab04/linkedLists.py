class Node():
	def __init__(self, value, next=None):
		self.value=value
		self.next=next
	
	def __str__(self):
		return str(self.value)

class LinkedList():
	def __init__(self, head=None):
		self.head=head
	
	def add(self, value):
		newNode = Node(value, self.head)
		self.head=newNode
	
	def addNode(self, node):
		node.next = self.head
		self.head = node
	
	def indexOf(self, value):
		index=0
		current = self.head
		while (current):
			if current.value==value:
				return index
			else:
				current = current.next
				index+=1
		raise ValueError(f'{value} is not in the list.')
	
	def traverse(self, f):
		current=self.head
		while (current):
			f(current.value)
			current=current.next

	def toList(self):
		returnList=[]
		current=self.head
		while (current):
			returnList.append(current.value)
			current=current.next
		return returnList

	# first attempt, with O(k*n) complexity
	def kthLastNaive(self, k):
		current=self.head
		while (current):
			kth = current
			
			#look ahead k positions
			for i in range(0,k):
				if kth.next:
					kth = kth.next
				else:
					raise OverflowError(f'List is shorter than {k}')
			
			#if k is null, current is the solution
			if not kth.next:
				return current.value
			current = current.next
	
	# second attempt, with O(2n-k) complexity
	def kthLast(self, k):
		nCurrent = self.head
		kCurrent = nCurrent
		
		#find element k positions away
		for i in range(k+1):
			if kCurrent.next:
				kCurrent = kCurrent.next
			else:
				raise OverflowError(f'List is shorter than {k}')
		
		#advance both pointers together
		while (kCurrent):
			kCurrent = kCurrent.next
			nCurrent = nCurrent.next
		
		return nCurrent
	
	@staticmethod
	def reverse(list):
		outList = LinkedList()
		current = list.head
		
		while current:
			next = current.next
			outList.addNode(current)
			current = next
		list.head = outList.head
		
		return
	
	def partition(self, predicate):
		trueList = LinkedList()
		falseList = LinkedList()
		
		current=self.head #load first element
		mid = current #save head to link to other list
		
		while (current):
			
			next=current.next #load next element before changing current reference
			
			if predicate(current.value):
				trueList.addNode(current)
				
			else:
				falseList.addNode(current)
			
			current=next
			
		if predicate(mid.value): #determine which list contains the original head
			mid.next = falseList.head
			self.head = trueList.head
			return trueList
		
		else:
			mid.next = trueList.head
			self.head = falseList.head
			return falseList