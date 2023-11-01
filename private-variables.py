
def modify_local_var():
    local_var = 5  # ตัวแปร Local
    local_var = local_var + 1  # แก้ไขค่า Local variable
    print("Local Variable (inside function):", local_var)

modify_local_var()  # ผลลัพธ์: Local Variable (inside function): 6

local_var = 10
print(local_var)
