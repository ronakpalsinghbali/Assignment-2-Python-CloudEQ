# Using append() by converting tuple into list.

mytup = ("Ronak", 25, "India", "Male")
print(type(mytup))
print(mytup)

mylist = list(mytup)  # converting tuple into a list.
print(type(mylist))


mylist.append("Jammu and Kashmir")  # using append() on list.

mytup = tuple(mylist)  # converting list back to tuple.

print(mytup)
print(type(mytup))
