# Program to sort alphabetically the words form a string provided by the user


comment=input("Enter your string: ").lower()
words=comment.split(" ")
words.sort()
print("The sorted words are: ")
for word in words:
    print(word)