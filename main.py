#questions
import sqlite3 as sql

personality = {'p1':1, 'p2':1, 'p3':1}

questions_and_answers = []

name = input("ENTER YOUR NAME!")

scenarios = open('quetions.txt', 'r')
questions = scenarios.readlines()

for question in questions:
    question = question.strip()
    questions_answers = question.split(";")
    print (questions_answers[0])
    print("")
    a = print(questions_answers[1])
    b = print(questions_answers[2])
    c= print(questions_answers[3])


    answer = (input("your answer? "))
    if answer == "a":
        personality["p1"] = personality["p1"] + 1
            #temp = personality['p1']
            #temp = temp + 1
            #personality['p1'] = temp
    if answer == "b":
            personality['p2'] = personality['p2'] + 1
    if answer == c:
            personality['p3'] = personality['p3'] + 1

    if personality["p1"] > personality["p2"] or personality["p1"] > personality["p3"]:
        personalityResult = "P1"

    elif personality["p2"] > personality["p1"] or personality["p2"] > personality["p3"]:
        personalityResult = "P2"

    elif personality["p3"] > personality["p1"] or personality["p3"] > personality["p2"]:
        personalityResult = "P3"






#if personality["p3"] == personality["p3"] +1:


#trying to add sub category
     

print ("you are " + personalityResult)
print(personality)




con = sql.connect("database.db")
cur = con.cursor()
cur.execute(
    "INSERT INTO TestResults (Names,Results) VALUES (?,?)",
                (name, personalityResult)
            )
con.commit()
con.close()



    





