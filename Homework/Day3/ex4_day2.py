score_three = 50
score_four = 70
score_five = 85

student_score = int(input("Provide student score"))

if student_score < 50:
 print("Failed")
elif student_score >= 50 and student_score < 70:
 print("3")
elif student_score >=70 and student_score < 85:
 print("4")
else:
 print("5")
