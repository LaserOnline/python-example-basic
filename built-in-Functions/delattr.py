
# * สร้างคลาส Coordinate และกำหนดค่าของตัวแปร x, y, z
class Coordinate:
    x = 10
    y = -5
    z = 0

# * สร้างอ็อบเจกต์ point1 จากคลาส Coordinate
point1 = Coordinate()

# * แสดงค่าของ x, y, และ z ที่อยู่ในอ็อบเจกต์ point1
print('x = ', point1.x)
print('y = ', point1.y)
print('z = ', point1.z)

# * ใช้ delattr() เพื่อลบแอตทริบิวต์ z ออกจากคลาส Coordinate
delattr(Coordinate, 'z')

# * แสดงผลลัพธ์หลังจากลบแอตทริบิวต์ z ออก
print('--After deleting z attribute--')
print('x = ', point1.x)
print('y = ', point1.y)

# * พยายามแสดงค่าของแอตทริบิวต์ z ที่ถูกลบ
print('z = ', point1.z)