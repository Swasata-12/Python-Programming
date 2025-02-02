phone=input("Enter Phone No. : ")
digit_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
output=""
for ch in phone:
    output += digit_mapping.get(ch,"!") + " "
    # output += digit_mapping[ch,"!"] + " "      # this technique cann't work here
print(output)