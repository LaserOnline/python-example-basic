
value = input("Enter Number : ")
# * isdigit เพื่อตรวจสอบว่าสตริงนั้นประกอบด้วยตัวเลขเท่านั้นหรือไม่ โดยจะคืนค่า True ถ้าสตริงนี้ประกอบด้วยตัวเลขเท่านั้น และคืนค่า False
if value.isdigit():
    value = int(value)
    
    if value >= 80:
        print("A")
    elif value >= 70:
        print("B")
    elif value >= 60:
        print("C")
    elif value >= 40:
        print("D")
    else:
        print("F")

else:
    print("Error Get Number")