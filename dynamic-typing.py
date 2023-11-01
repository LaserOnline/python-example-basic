
# * ฟังก์ชันสำหรับรับค่าและแสดงผล
def process_input(input_value):
    if isinstance(input_value, int):
        print(f"ค่าที่รับเข้ามาเป็นตัวเลข (int): {input_value}")
    elif isinstance(input_value, str):
        print(f"ค่าที่รับเข้ามาเป็นข้อความ (str): {input_value}")
    elif isinstance(input_value, float):
        print(f"ค่าที่รับเข้ามาเป็นทศนิยม (float): {input_value}")
    else:
        print("ไม่รู้จักชนิดข้อมูลนี้")

# * รับค่าจากคีย์บอร์ด
user_input = input("โปรดป้อนค่า: ")

# * ลองแปลงค่าที่รับเข้ามาเป็น int หรือ float
try:
    user_input = int(user_input)
except ValueError:
    try:
        user_input = float(user_input)
    except ValueError:
        pass

# * เรียกใช้ฟังก์ชันเพื่อแสดงผลลัพธ์
process_input(user_input)
