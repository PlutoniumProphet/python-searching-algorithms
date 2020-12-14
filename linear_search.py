# Linear search is rarely used practically because other search algorithms 
# such as the binary search algorithm and hash tables allow significantly 
# faster-searching comparison to Linear search.

# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def search(arr, n, x):

	for i in range(0, n):
		if (arr[i] == x):
			return i
	return -1


# Driver Code
arr = [2, 3, 4, 10, 40, 101]
x = 4
n = len(arr)

# Function call
result = search(arr, n, x)
if(result == -1):
	print(f"Element {x} is not present in array")
else:
	print(f"Element {x} is present at index {result}")


