from doctest import Example


print("Grading System") ; print("")


#asking input from user.  
quiz1 = int(input("Please enter the score of the first quiz: "))
quiz2 = int(input("Please enter the score of the seccond quiz: "))
quiz3 = int(input("Please enter the score of the third quiz: "))
recitation1 = int(input("Please enter the score of the recitation: "))
exam1 = int(input("Please enter the score of the exam: "))

#grade system.
quizTotal = quiz1 + quiz2 + quiz3 ; quizDec = quizTotal / 30 ; quizPnts = quizDec * 100
reciDec = recitation1 / 100 ; reciPnts = reciDec * 100
examDec = exam1 / 50 ; examPnts = examDec * 100
totalAve = quizPnts + reciPnts + examPnts ; totalPerc = totalAve / 300
totalAvePerc = "{:.2%}".format(totalPerc)
print(totalAvePerc)


