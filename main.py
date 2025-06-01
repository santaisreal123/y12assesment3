#questions
import sqlite3 as sql
from question_class import testq
File = open("quetions.txt", "r")

questions = File.read()
print(questions)

personality = {'p1':1, 'p2':1, 'p3':1} 

name = input("ENTER YOUR NAME!")

for i in questions:
      

print("scenario")
print("a")
print("b")
print("c")
answer1 = (input("your answer? "))
if answer1 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer1 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer1 == ("c"):
    personality['p3'] = personality['p3'] + 1


print("scenario")
print("a")
print("b")
print("c")
answer2 = (input("your answer? "))
if answer2 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer2 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer2 == ("c"):
     personality['p3'] = personality['p3'] + 1

print("scenario")
print("a")
print("b")
print("c")
answer3 = (input("your answer? "))
if answer3 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer3 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer3 == ("c"):
     personality['p3'] = personality['p3'] + 1

print("scenario")
print("a")
print("b")
print("c")
answer4 = (input("your answer? "))
if answer4 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer4 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer4 == ("c"):
     personality['p3'] = personality['p3'] + 1

print("scenario")
print("a")
print("b")
print("c")
answer5 = (input("your answer? "))
if answer5 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer5 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer5 == ("c"):
     personality['p3'] = personality['p3'] + 1

print("scenario")
print("a")
print("b")
print("c")
answer6 = (input("your answer? "))
if answer6 == ("a"):
    personality['p1'] = personality['p1'] + 1
if answer6 == ("b"):
    personality['p2'] = personality['p2'] + 1
if answer6 == ("c"):
     personality['p3'] = personality['p3'] + 1

if personality["p1"] > personality["p2"] or personality["p1"] > personality["p3"]:
    personalityResult = "P1"


elif personality["p2"] > personality["p1"] or personality["p2"] > personality["p3"]:
    personalityResult = "P2"


elif personality["p3"] > personality["p1"] or personality["p3"] > personality["p2"]:
        personalityResult = "P3"

#sub categories
if personality["p2"] > 1 and personality["p1"] > personality["p3"]:
        personalityResult = "P1+P2"


if personality["p1"] > 1 and personality["p2"] > personality["p3"]:
        personalityResult = "P2+P1"       


if personality["p3"] > 1 and personality["p1"] > personality["p2"]:
        personalityResult = "P1+P3"


if personality["p1"] > 1 and personality["p3"] > personality["p2"]:
        personalityResult = "P3+P1"


if personality["p3"] > 1 and personality["p2"] > personality["p1"]:
        personalityResult = "P2+P3"


if personality["p2"] > 1 and personality["p3"] > personality["p1"]:
        personalityResult = "P3+P2"


if personality["p1"] > 1 and personality["p2"] > personality["p3"]:
        personalityResult = "P2+P1"


if personality["p2"] > 1 and personality["p1"] > personality["p3"]:
        personalityResult = "P1+P2"


if personality["p2"] > 1 and personality["p3"] > personality["p1"]:
        personalityResult = "P3+P2"


if personality["p3"] > 1 and personality["p2"] > personality["p1"]:
        personalityResult = "P2+P3"


if personality["p1"] > 1 and personality["p3"] > personality["p2"]:
        personalityResult = "P3+P1"


if personality["p3"] > 1 and personality["p1"] > personality["p2"]:
        personalityResult = "P1+P3"




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



    





