customer={
    "Name":"Swasata Nandy",
    "Age":30,
    "is_verified":True
}
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

merged=customer|digit_mapping
print(merged)