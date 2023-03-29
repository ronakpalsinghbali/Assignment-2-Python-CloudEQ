# Accessing an element in SET{}
# We cannot use indexing as sets are unordered but we can use different ways to access elements in set.
# One is using 'in' keyword to loop through a set.

myset = {"green","yellow","orange","brown","blue","red","purple"}

for x in myset:
    print(x)

# we can you 'in' keyword to check if an item is present in set or not.
# if the item is prsent in the set it will print true ,else will print false.
print("green" in myset)


# Second is converting the set into a list and then accessing the items

mylist = list(myset)
print(mylist[-7:])


#Third is using pop(), tihs will pop a random item from the set

print(myset.pop())


