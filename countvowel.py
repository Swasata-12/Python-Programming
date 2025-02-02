# Program to count the number of each vowels

comment=input("Enter your string: ").lower()
count=0
for ch in comment:
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        count+=1
print(f"Total no of vowels in your string is {count}")


# Another approach

vowels="aeiou"
ip_str="Hello, have you tried our tutorial section yet?"
ip_str=ip_str.casefold()            # make it suitable for caseless comparisions
count={}.fromkeys(vowels,0)         # make a dictionary with each vowel a key and value 0
for char in ip_str:
    if char in count:
        count[char]+=1
print(count)