# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’

f=open("poem.txt")
text=f.read()
if("twinkle" in text):
    print("Your text is present")
else:
    print("Not present")
f.close()