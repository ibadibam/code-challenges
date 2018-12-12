#!/usr/bin/env python

"""ArrayReverse.py: Exercises in array reversal.
For Lab01 of seattle-dsa-501d3"""

__author__	= "Adam Berey"
__date__   	= "2018-12-10"

#helper function for testing
def printOk(f, arg, expected):
	works = "ok" if (f(arg) == expected) else "failed"
	print(f"{f.__name__} {works}")

def pythonicReverse(arr):
	return arr[::-1] #'pythonic' approach

def quickReverse(arr):
	newArr = []
	for e in arr[::-1]:
		newArr.append(e)
	return newArr

def noSliceReverse(arr):
	newArr = []
	for i in range (len(arr)-1, -1, -1):
		newArr.append(arr[i])
	return newArr

def recursiveReverse(inArr, outArr=[]):
	
	if inArr:
		outArr.append(inArr.pop())
		return recursiveReverse(inArr, outArr)
	else:
		return outArr

def main():
	testArr=[1,2,3]
	tgtArr=[3,2,1]

	printOk(pythonicReverse, testArr, tgtArr)
	printOk(quickReverse, testArr, tgtArr)
	printOk(noSliceReverse, testArr, tgtArr)
	printOk(recursiveReverse, testArr, tgtArr)

if __name__ == "__main__": main()