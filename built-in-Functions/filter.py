
# * สร้างฟังก์ชัน check_even() ที่รับตัวแปร number และตรวจสอบว่าเป็นเลขคู่หรือไม่
def check_even(number):
    if number % 2 == 0:
        return True
    return False

# * สร้างรายการ (list) numbers ที่ประกอบด้วยตัวเลขต่าง ๆ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# * ใช้ฟังก์ชัน filter() เพื่อสร้างอ็อบเจกต์ที่เก็บเฉพาะตัวเลขคู่จากรายการ numbers
even_numbers_iterator = filter(check_even, numbers)

# * แปลงอ็อบเจกต์ even_numbers_iterator เป็นรายการ (list) และเก็บตัวเลขคู่ในรายการ even_numbers
even_numbers = list(even_numbers_iterator)

# * แสดงผลลัพธ์ที่เก็บในรายการ even_numbers
print(even_numbers)
