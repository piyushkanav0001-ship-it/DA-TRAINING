a={"Aman":99,"karan":85,"piyush":76,"harash":88}
for student in a:
    if a[student]>=35 and a[student]<60:
        print(f"{student} has scored {a[student]} marks and has grade C")
    elif a[student]>=60 and a[student]<80:
        print(f"{student} has scored {a[student]} marks and has grade B")   
    elif a[student]>=80:
        print(f"{student} has scored {a[student]} marks and has grade A")
    else:
        print(f"{student} has scored {a[student]} marks and has failed")
  
