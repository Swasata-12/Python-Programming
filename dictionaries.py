customer={
    "Name":"Swasata Nandy",
    "Age":30,
    "is_verified":True
}
print(customer["Name"])                         # accessing the key of the dictionary
print(customer["Age"])
print(customer.get("Name"))                     # accessing the key of the dictionary using get method
print(customer.get("is_verified"))
print(customer.get("birthdate"))                # for key not in dictionary return none
print(customer.get("birthdate","Jan 9 1999"))   # assign value to the key not present in dictionary
customer["birthdate"]="June 12 1999"            # assign value to the key not present in dictionary
print(customer["birthdate"])
customer["Name"]="John Smith"                   # can change the key value like this
print(customer["Name"])
print(customer.get("fav_colour","!"))           # if the key value present in dictionary then return that
                                                # value unless return !
print(customer)
print(len(customer))

# Delete an Element From a Dictionary

my_dict = {31: 'a', 21: 'b', 14: 'c'}
del my_dict[31]
print(my_dict.pop(21))    # returns the value assiciated to the key
print(my_dict)