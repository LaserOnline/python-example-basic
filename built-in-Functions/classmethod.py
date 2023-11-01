
# * สร้างคลาส Student
class Student:
    marks = 0

    # * สร้างเมธอด compute_marks ที่ใช้ในการคำนวณและพิมพ์คะแนนที่ได้
    def compute_marks(self, obtained_marks):
        marks = obtained_marks
        print('Obtained Marks:', marks)

# * สร้างเมธอด print_marks ในรูปแบบเมธอดคลาส (classmethod) โดยใช้ @classmethod เพื่อเป็นการเชื่อมโยงกับ compute_marks
Student.print_marks = classmethod(Student.compute_marks)

# * เรียกใช้เมธอด print_marks โดยส่งค่าพารามิเตอร์ 88 เพื่อคำนวณและแสดงผลลัพธ์
Student.print_marks(88)
