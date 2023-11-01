
# * สร้างรายการ (list) grocery
grocery = ['bread', 'milk', 'butter']

# * ใช้ฟังก์ชัน enumerate() เพื่อสร้างอ็อบเจกต์ที่มีคู่ค่า (index, value) ของรายการ grocery
enumerateGrocery = enumerate(grocery)

# * แสดงประเภทของอ็อบเจกต์ enumerateGrocery
print(type(enumerateGrocery))

# * แปลงอ็อบเจกต์ enumerateGrocery เป็นรายการ (list) และแสดงผลลัพธ์
print(list(enumerateGrocery))

# * ใช้ฟังก์ชัน enumerate() อีกครั้งแต่ระบุค่าเริ่มต้นของ index เป็น 10
enumerateGrocery = enumerate(grocery, 10)

# * แปลงอ็อบเจกต์ enumerateGrocery เป็นรายการ (list) และแสดงผลลัพธ์
print(list(enumerateGrocery))