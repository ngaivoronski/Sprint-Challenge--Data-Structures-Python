import time

start_time = time.time()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Find if the value is already in the tree
    def dupeFind(self, value):
        if value > self.value:
            if self.right is None:
                pass
            else:
                self.right.dupeFind(value)
        elif value < self.value:
            if self.left is None:
                pass
            else:
                self.left.dupeFind(value)
        # If the value is in the tree, add it to the duplicates array
        else:
            duplicates.append(value)

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
binaryTree = BinarySearchTree("l")

for name in names_1:
    binaryTree.insert(name)
for name in names_2:
    binaryTree.dupeFind(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"original runtime using data structure: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# create a new set to remove internal duplicates
newSet = {"asdf"}

# create a new duplicates array
dupes2 = []

# fill out the set with the values from names_1
for name in names_1:
    newSet.add(name)

# use built-in sort function to sort the new set
newSet2 = sorted(newSet)

# binary search function
def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

# run binary search on each name in names_2
for name in names_2:
    if BinarySearch(newSet2, name) >= 0:
        dupes2.append(name)

# print endtime
end_time2 = time.time()
print (f"runtime using built-in sorted function: {end_time2 - end_time} seconds")