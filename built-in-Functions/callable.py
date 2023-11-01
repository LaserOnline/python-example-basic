
# * กำหนดค่าตัวแปร x เป็น 5
x = 5

# * ใช้ callable() เพื่อตรวจสอบว่า x สามารถเรียกใช้ได้หรือไม่
print(callable(x))

# * นี่คือฟังก์ชัน testFunction ที่ใช้ในการพิมพ์ "Test"
def testFunction():
  print("Test")

# * กำหนดตัวแปร y เป็นอ้างอิงไปยังฟังก์ชัน testFunction
y = testFunction

# * ใช้ callable() เพื่อตรวจสอบว่า y สามารถเรียกใช้ได้หรือไม่
print(callable(y))
