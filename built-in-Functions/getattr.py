
# * สร้างคลาส Student ที่มีแอตทริบิวต์ marks และ name
class Student:
    marks = 88
    name = 'Sheeran'

# * สร้างอ็อบเจกต์ person จากคลาส Student
person = Student()

# * ใช้ฟังก์ชัน getattr() เพื่อเข้าถึงแอตทริบิวต์ 'name' ของอ็อบเจกต์ person
name = getattr(person, 'name')
print(name)  # * ผลลัพธ์คือ 'Sheeran'

# * ใช้ฟังก์ชัน getattr() เพื่อเข้าถึงแอตทริบิวต์ 'marks' ของอ็อบเจกต์ person
marks = getattr(person, 'marks')
print(marks)  # * ผลลัพธ์คือ 88