
# * กำหนดค่าของตัวแปร age เป็น 23
age = 23

# * ใช้ฟังก์ชัน globals() เพื่อเข้าถึงตัวแปรในส่วนของ global scope และปรับค่าของตัวแปร age เป็น 25
globals()['age'] = 25

# * แสดงผลลัพธ์โดยใช้ตัวแปร age หลังจากการเปลี่ยนค่า
print('The age is:', age)
