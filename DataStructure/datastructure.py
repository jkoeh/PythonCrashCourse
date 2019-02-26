# zip function
from array import array
from collections import deque
from sys import getsizeof
zipList1 = [1, 2, 3, 4, 5]
zipList2 = ['a', 'b', 'c', 'd', 'e']
zipTupleList = list(zip(zipList1, zipList2))
print(zipTupleList)

# queue, handle first in first out
queue = deque([('a', 10), ("b", 9), ('c', 12)])
queue.popleft()
print(queue)


# array, use it to optimize list if the performance doesn't meet req
# the first parameter is a python typecode that indicate and enforce the type of the array
arrayEx = array("i", (1, 2, 3))
arrayEx.append(4)
print(arrayEx[-1])


# set: datastructure that is a unordered collection of data without dup. like hashset. no indexing.
setnum = [1, 1, 2, 3, 4]
firstUniq = set(setnum)  # or
secUniq = {1, 5}
print(firstUniq)

# join two sets, only unique
print(firstUniq | secUniq)

# intersection of two sets
print(firstUniq & secUniq)

# first second minus second sets
print(firstUniq - secUniq)

# in either but not both
print(firstUniq ^ secUniq)

# dictionary comprehesion: use a comprehesion to construct a dictionary from a list according to certain logic
listForDictComp = [1, 2, 3, 3, 4, 5]
dictComp = {x: x*2 for x in listForDictComp}
print(dictComp)

# generator
# It is used to saved memory when we have to iterate through large or potentially
# infinite number of data. In that case, we do not want to store the
# whole list inside memory as it would be inefficient use of memory. So we use
# generator to iterate through the data list instead. the memory usage stays constant
# and there's no length for generator.
genVals = (x*2 for x in range(100))
print("gen: ", getsizeof(genVals))
for gen in genVals:
    print(gen)


# unpacking (like the spread operator in js), the coolest thing is that you could upack any 
# iterable such as range or tuple, list, dictionary, string. we can also use it to combine 
# multiple iterable by unpacking each of them in a single lis
numbers =[1,2,3]
print("without spread: ", numbers)
print("with spread: ", *numbers)
print(*range(5))
print(*('t', 'u'))
print(*(('t', 'u'), ('p', 'l')))

# when combining dictionary, the last value of the same key will be used. in this case x will 
# be 'b' in combinedDict
firstDict={'x': 'a'}
secondDict={'x': 'b', 'y': 'c'}
combinedDict={**firstDict, **secondDict, "z": 'd'}
print(combinedDict)