list=[0.0,0.0,0.0,100,0.0,0.0]              #Data list

list[0] = 50.0                              #<--- Change the Amount of Questions
list[1] = 10.0                              #<--- Change the Amount of Wrong Answers

print("Total Q" , list[0])                  #Print the Amount of Questions
print("Wrong A" , list[1])                  #Print the Amount of Wrong Answers

if list[1] == 0:                            #Condition 100% rules devide 0
    list[2] = list[0]
elif list[1] != 0:
    list[2] = list[0] / list[1]

print("Ratio  " , list[2])                  #Print Ratio

if list[1] == 0:                            #Condition 100% rules devide 0
    list[4] = list[1]
elif list[1] != 0:
    list[4] = list[3] / list[2]

list[4] = list[3] - list[4]                 #Math Calc Score

print("Score  " , list[4],"%")              #Print Score
print()                                     #Print Empty Line
print("You have a score of ", list[4]/10)   #Print Score

if list[4] < 80.0:                          #Condition Score Check 
    print("Sorry you failed")               #Print Fail
elif list[4] == 80.0:                       #Condition Score Check
    print("Yeah you passed the test")       #Print Pass
elif list[4] > 80.0:                        #Condition Score Check
    print("Yeah you passed the test")       #Print Pass
if list[4] == 100.0:                        #Condition Flawless Check
    print("Flawless")                       #Print Flawless
