marks = int(input("enter your marks in subject:"))
if 90 < marks <= 100:
    print("grade: Excellent")
elif 80 < marks <= 90:
    print("grade: A")
elif 70 < marks <= 80:
    print("grade: B")
elif 60 < marks <= 70:
    print("grade: C")
elif 50 < marks <= 60:
    print("grade: D")
elif 0  < marks <= 50:
    print("grade: F")
else:
    print("invalid marks")
