# Write a python function to remove a given word from a list ad strip it at the same time.

def remove(l,word):
    n=[]
    for item in l:
        if(item!=word):
            n.append(item.strip(word))
    return n


l=[]
for i in range(5):
    name=input(f"Enter {i+1} name: ").title()
    l.append(name)
word=input("Enter the word which you want to strip: ")
print(remove(l,word))