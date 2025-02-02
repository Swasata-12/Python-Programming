# Write a program to print third, fifth and seventh element from a list using enumerate function.

list=[1,2,3,"Harry","Rahul",25,47,"Swasata"]
for i,item in enumerate(list):
    if i==2 or i==4 or i==6:
        print(item)

# same problem without enumerate function
j=0
for item in list:
    if(j==2 or j==4 or j==6):
        print(list[j])
    j+=1