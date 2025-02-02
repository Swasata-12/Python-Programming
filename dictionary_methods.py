customer={
    "Name":"Swasata Nandy",
    "Age":30,
    "is_verified":True
}

print(customer.items())                 # Returns a list of (key,value)tuples.
print(customer.keys())                  # Returns a list containing dictionary's keys
print(customer.values())                # Returns a list containing dictionary's values
customer.update({"Age":22,"Gender":"Male"})             # Updates the dictionary with supplied key-value pairs and also can add new key value which is not present in it
print(customer)
print(customer.get("Name"))             # Returns the value of the specified keys
print(customer.get("marks"))            # this returns None
# print(customer["marks"])                # but this threw an error
customer.pop("Name")

if "Name" in customer:
    print("Present")