# Python Program to Remove Punctuations From a String

punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
strg=input("Enter your string: ")
newstrg=""
for ch in strg:
    if ch not in punctuations:
        newstrg+=ch
print(newstrg)