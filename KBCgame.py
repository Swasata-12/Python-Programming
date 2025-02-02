# Create a program capable of displaying questions to the user like KBC. Use list datatype to store the 
# questions and their correct answers. Display the final ammount the person is taking home after game.

questions=[["Which language was used to create fb?","Python","French","Javascript","php","None",4],
           ["Which language was used to create fb?","Python","French","Javascript","php","None",4],
           ["Which language was used to create fb?","Python","French","Javascript","php","None",4],
           ["Which language was used to create fb?","Python","French","Javascript","php","None",4],
           ["Which language was used to create fb?","Python","French","Javascript","php","None",4]
           ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
for i in range(len(questions)):
    question=questions[i]
    print(f"\n\nQuestions for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}     b.{question[2]}")
    print(f"c.{question[3]}     d.{question[4]}")
    reply=int(input("Enter your answer (1-4): "))
    if(reply==question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer!")
        break
print(f"Your take home money is {money}")