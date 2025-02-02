# Write a python program to translate a message into secret code language. Use the rules below:
# Coding: if the word contains atleast 3 characters remove the first letter annd append it at the end. Now 
# append three random characters at the starting and the end else simply reverse the string.
# Decoding: if the word contains less than 3 characters reverse it else remove 3 random characters from 
# start and end. Now remove the last letter and append it to the beginning.

message=input("Enter your message: ")
words=message.split(" ")
coding=input("1 for Coding or 0 for Decoding: ")
coding=True if (coding=="1") else False
print(coding)
if(coding):
    newwords=[]
    for word in words:
        if(len(word)>=3):
            r1="dsk"
            r2="jkr"
            stnew=r1+word[1:]+word[0]+r2
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))

else:
    newwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" ".join(newwords))