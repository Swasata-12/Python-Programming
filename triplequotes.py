statement="Swasata's pet name is Rocky"
print(statement)
course = '''
Hi Swasata,
Here is our first email to you.
Thank you,
The support team.
'''
print(course)                     # here the quotations may be in single quotes or in double quotes("""""")

name='Swasata'
print(len(name))
print(name[0])                    # just like printing the first element of the character array
print(name[-1])                    
print(name[-2])                    
print(name[0:3])                  # starting from 0th location to 2nd location

another = name[:]                 # copy one string to another
print("another = "+another)
print(f"another = {another}")
print(name[1:-1])
print(name[::-1])                 # reverse a string