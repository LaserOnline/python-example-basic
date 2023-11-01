
# * สร้างข้อความ codeInString ที่มีโค้ด Python ภายใน
codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'

# * ใช้ฟังก์ชัน compile() เพื่อแปลงโค้ดใน codeInString เป็นวัตถุรหัส Python ในรูปแบบ 'exec'
# * โดยระบุ 'sumstring' เป็นชื่อโค้ดและ 'exec' เป็นโหมดการแปลงโค้ด
codeObject = compile(codeInString, 'sumstring', 'exec')

# * ใช้ฟังก์ชัน exec() เพื่อรันโค้ดที่ถูกแปลงเป็น codeObject
exec(codeObject)
