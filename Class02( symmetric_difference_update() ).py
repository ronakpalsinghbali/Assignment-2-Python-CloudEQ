# Using Symmetric_difference_update().

set1 = {"apple","mango","banana","orange"}

set2 = {"apple","grapes","banana","orange","pineapple"}


set1.symmetric_difference_update(set2) # This method removes the item that is present in both sets and adds the item that is not present in both the sets in the first set.

# This method removed "apple","banana","orange" and added "pineapple" in the first set

print(set1)

