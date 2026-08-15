total_marks = int(input("enter your total percentage of your three subjects:"))
subject1 = int(input("enter your subject1 percent:"))
subject2 = int(input("enter your subject2 percent:"))
subject3 = int(input("enter your subject3 percent:"))
if total_marks > 100 or subject1 > 100 or subject2 > 100 or subject3 > 100:
    print("enter valid percent")
elif total_marks < 40 or subject1 < 33 or subject2 < 33 or subject3 < 33: 
    print("fail")
else:
    print("pass")
