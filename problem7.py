# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

fav_language={}
for i in range(4):
    name=input("Enter your friends name: ")
    lang=input("Enter language name: ")
    fav_language.update({name: lang})
print(fav_language)
