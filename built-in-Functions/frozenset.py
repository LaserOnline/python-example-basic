
# * สร้างเซตแบบไม่เปลี่ยนแปลง (frozenset) A, B, และ C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# * ใช้เมธอด isdisjoint() เพื่อตรวจสอบว่าเซต A และ C ไม่มีสมาชิกร่วมกันหรือไม่
print(A.isdisjoint(C))  #*  ผลลัพธ์คือ True เนื่องจาก A และ C ไม่มีสมาชิกร่วมกัน

# * ใช้เมธอด issubset() เพื่อตรวจสอบว่าเซต C เป็นเซตย่อยของเซต B หรือไม่
print(C.issubset(B))  # * ผลลัพธ์คือ True เนื่องจาก C เป็นเซตย่อยของ B

# * ใช้เมธอด issuperset() เพื่อตรวจสอบว่าเซต B เป็นเซตย่อยของเซต C หรือไม่
print(B.issuperset(C))  # * ผลลัพธ์คือ True เนื่องจาก B เป็นเซตย่อยของ C
