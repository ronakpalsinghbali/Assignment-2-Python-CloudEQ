# Difference between Discard() and Remove()


# Discard(), this function will not throw an error if the item is not present in the SET.

myset = {"green","yellow","orange","brown","blue","red","purple"}
print(myset)

myset.discard("pink")
print(myset)

# Remove(), this function will throw an error if the item is not present in the SET.

myset.remove("pink")
print(myset)
