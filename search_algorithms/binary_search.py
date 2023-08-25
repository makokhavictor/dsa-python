import math
'''
- Define two pointers (low and high)
- Calculate mid = (low + high) /2 Floor value
- If element at mid is not target, check if element at mid is greater than target
- If so, then target is on the left
- Set high to be mid - 1
- Repeat the step above
- If element at mid is less than target, then target is on the right.
- Set low to be mid + 1
- Repeat the steps above
- If high equals low and element is not same as target, it means target does not exist in the list.
- The array must be sorted
- Stop when you have found the target or when low > high
'''
def binary_search_iterative(haystack, needle):
    left = 1
    end = len(haystack)
    
    while (left <= end):
        middle = math.floor((left + end)/2)
        print(f'middle point is {middle}')
        if(haystack[middle] == needle):
            print(f'Element {needle} found at index {middle}')
            return middle
        elif (needle < haystack[middle]):
            print('Element is on the left')
            end = middle - 1
        elif (needle > haystack[middle]):
            print('Element is on the right')
            left = middle + 1
    print('Element not found')
    return -1
    





if __name__ == '__main__':
    indexOfElement = binary_search_iterative([11,12,13,14,15], 13)
    print(indexOfElement)
