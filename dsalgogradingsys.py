from doctest import Example


print("Grading System") ; print("")


#asking input from user.  
quiz1 = int(input("Please enter the score of the first quiz: "))
quiz2 = int(input("Please enter the score of the seccond quiz: "))
quiz3 = int(input("Please enter the score of the third quiz: "))
recitation1 = int(input("Please enter the score of the recitation: "))
exam1 = int(input("Please enter the score of the exam: "))

#grade system.
quizTotal = quiz1 + quiz2 + quiz3 ; quizDec = quizTotal / 30 ; quizPnts = quizDec * 30
reciDec = recitation1 / 100 ; reciPnts = reciDec * 30
examDec = exam1 / 50 ; examPnts = examDec * 40
totalAve = quizPnts + reciPnts + examPnts ; totalPerc = totalAve / 100
totalAvePerc = "{:.2%}".format(totalPerc)
print(totalAvePerc)


