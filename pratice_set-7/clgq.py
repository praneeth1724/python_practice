eng = int(input("enter your english marks:"))
tel = int(input("enter your telugu marks:"))
math =  int(input("enter your math marks:"))
social =  int(input("enter your social marks:"))
hindi =  int(input("enter your hindi marks:"))
science =  int(input("enter your science marks:"))
total_marks = eng + tel + math + social + hindi + science
average = total_marks / 6
if eng >= 35 and tel >= 35 and math >= 35 and social >= 35 and hindi >= 35 and science >= 35:
    print("he has passed all subjects")
    if total_marks > 500:
        print("total marks are:",total_marks)
        print("average is:",average)
        print("First class")
    elif total_marks > 400 and total_marks < 500:
        print("total marks are:",total_marks)
        print("average is:",average)
        print("Second class")
    elif total_marks > 300 and total_marks < 400:
        print("total marks are:",total_marks)
        print("average is:",average)
        print("Third class")
    elif total_marks < 300:
        print("fail")
    else:
        print("invalid input")
else:
    print("fail")


