# Using intersection_update().

set1 = {"apple","mango","banana","orange"}

set2 = {"apple","grapes","banana","orange","pineapple"}

set1.intersection_update(set2) # This method removes the item that is not present in both the sets.
# This methos removed "mango and "grapes" as the are not present in both the sets.
print(set1)