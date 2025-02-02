course = "There was a man in the house"
print(len(course))                      # calculate the no of charecters in a string
print(course.upper())                   # convert the given string in upper case
print(course.lower())                   # convert the given string in lower case
print(course)                           # string methods can't change the actual string rather copy a string and make changes on that
print(course.find("man"))               # find if the given part of the string present in the string
print(course.endswith("rry"))           # tells whether the variable string ends with the string "rry" or not
print(course.startswith("ha"))
print(course.count("a"))                # count the no of given char in the string
print(course.find("h"))                 # return the index no of the given character on the string
print(course.replace("man","ghost"))    # replace the 1st part by 2nd part 
print(course.replace("m","v"))          # replace the first character by 2nd character
print("man" in course)                  # return a boolean value True or False if the str present 
print(course.title())                   # each word of the string starts with uppercase
numbers="123456789"
print(numbers[1:7:3])                   # Slicing with skip value 
print(numbers[::-1])                    # Reverse a string
words=course.split(" ")                 # Split the string in list of words 
print(words)
print(course.strip("use"))                # stripe the given char from the string

# There is a difference between a general purpose function and a method. When a function is particularly
# specific to an object or expression then it is called a method. There is a difference at find and in function
# in line 6 and 10 find returns the index no from where the sub string starting, but in returns the boolean
# value if the sub string present in the actual string by True or False. 