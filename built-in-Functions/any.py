boolean_list = ['True', 'False', 'True']

# * ผลลัพธ์คือ True เพราะมีอย่างน้อยหนึ่งสมาชิกที่เป็น True
result = any(boolean_list)
print(result)

# * Output: True