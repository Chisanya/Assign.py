#Exam score grading
greeting = "Welcome to Learnfactory"
Students_name = input(f"Enter your name: ")
print(f"{Students_name}! {greeting}")
exam_score = float(input("Enter your exam score: "))

if exam_score <=0 or exam_score > 100:
        print(f"{Students_name} your {exam_score} is an invalid score")
else:
        if exam_score >=90 or exam_score ==100:
                print(f"{Students_name} your exam score is {exam_score}. You got A!") 
        elif exam_score ==80 or exam_score <=89:
                print(f"{Students_name} your exam score is {exam_score}. You got B!")
        if exam_score ==70 or exam_score <=79:
                print(f"{Students_name} your exam score is {exam_score}. You got C!") 
        if exam_score ==60 or exam_score <=69:
                print(f"{Students_name} your exam score is {exam_score}. You got D!") 
        if exam_score <60:
                print(f"{Students_name} your exam score is {exam_score}. You got F!") 
