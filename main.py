#questions
import sqlite3 as sql
personality = {'The Joker':1, 'The Sun':1, 'The Tower':1}
questions_and_answers = []

name = input("ENTER YOUR NAME!")

scenarios = open('quetions.txt', 'r')
questions = scenarios.readlines()

def personalityCheck(index):
    if questions_answers[index] == ' J':
        personality["The Joker"] = personality["The Joker"] +1
    elif  questions_answers[index] == ' T':
        personality["The Tower"] = personality["The Tower"] +1
    elif questions_answers[index] == ' S':
         personality["The Sun"] = personality["The Sun"] +1
    else: 
         print("can not record personality")
         

for question in questions:
    question = question.strip()
    questions_answers = question.split(";")
    print (questions_answers[0])
    print("")
    a = print(questions_answers[1])
    b = print(questions_answers[3])
    c= print(questions_answers[5])

  

    answer = (input("your answer? "))
    if answer == "a":
       index = 2
       personalityCheck(index)
    if answer == "b":
        index = 4
        personalityCheck(index)
    if answer == "c":
        index = 6
        personalityCheck(index)

    
    

if personality["The Joker"] > personality["The Tower"] and personality["The Joker"] > personality["The Sun"]:
    personalityResult = "The Joker"

elif personality["The Sun"] > personality["The Joker"] and personality["The Sun"] > personality["The Tower"]:
    personalityResult = "The Sun"

elif personality["The Tower"] > personality["The Joker"] and personality["The Tower"] > personality["The Sun"]:
    personalityResult = "The Tower"
    





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



    





