
## CS131 Assignment 2
## Prajwal Bhandari
## Jan 2024


def greatest_of_four(num1,num2,num3,num4): 
   
    if num1<num2: 
        largest1 = num2
    else: largest1 =num1 
    if num3<num4:
        largest2 =num4
    else: largest2 =num3
    if largest1<largest2:
        print (largest2, "is the largest number.")
        return largest2
    else:
        print (largest1, "is the largest number.")
        return largest1

#first scenario: two trains on a collision course
        
def determine_crash(velA,velB,dist):
    
    velA*=60    
    velB*=60
    #convert km to meters 
    dist*=1000
    velTotalmpm= velA-velB


    #determine crash function: 

    if velTotalmpm <= 0: 
        print("The trains are fine!")
    #put div by 0 error after code looks at the zero case so it doesnt run into it while executing
    else: 
        minutesToCrash= dist/(velTotalmpm)  
        print("Crash in", minutesToCrash , "minutes!")

#3.1 calculate final Grade: 

def final_percentage(Assignments,Exercises,DesDoc,KnowCheck,Exams,Final): 

    if Assignments <=0:
        Assignments =0  
    elif Assignments>=100:
        Assignments=100
    else: Assignments = Assignments
    #do the same for everything else.. make sure to account for all caxses.
    if Exercises<=0:
        Exercises=0
    elif Exercises>=100:
        Exercises=100
    else: Exercises=Exercises 
    if DesDoc<=0:
        DesDoc=0
    elif DesDoc>=100:
        DesDoc=100
    else: DesDoc=DesDoc
    if KnowCheck<=0:
        KnowCheck=0
    elif KnowCheck>=100:
        KnowCheck=100
    else: KnowCheck=KnowCheck
    if Exams<=0:
        Exams=0
    elif Exams>=100:
        Exams=100
    else: Exams=Exams
    if Final<=0:
        Final=0
    elif Final>=100:
        Final=100
    else: Final=Final
    #calculate the final grade out of 100 pts
#3.2 calculating a letter grade
    finalGrade = (Assignments*.14+Exercises*.16+DesDoc*.15+KnowCheck*.05+Exams*.25+Final*.25)
    print(finalGrade, "%", sep="")
    return finalGrade

def letter_grade(finalGrade):
    if finalGrade>1.0:
        LGrade="I"
    elif finalGrade>=.94:
        LGrade="A"
    elif finalGrade>=.90:
        LGrade="A-"
    elif finalGrade>=.87:
        LGrade="B+"
    elif finalGrade>=.84:
        LGrade="B"
    elif finalGrade>=.80:
        LGrade="B-"
    elif finalGrade>=.77:
        LGrade="C+"
    elif finalGrade>=.70: 
        LGrade="C"
    elif finalGrade>=.60:
        LGrade="D"
    elif finalGrade>=.0:
        LGrade="F"
    else: LGrade="I"  #accounts for final grade being greater than 1 or less than 0 ,
    print("Your final Grade is a ", LGrade, ".", sep="")
    

def main():
    # TODO; Test my functions
    greatest_of_four(1,2,3,4)
    determine_crash(0.0, -0.8018444813530503, 1.726800422470414)
    final_percentage(100,100,100,100,50,0)
    letter_grade(.23)

if __name__ == "__main__":
    main()

