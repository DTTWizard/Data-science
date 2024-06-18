#15_A
def greeting(full_name, birth_year):
    current_year = 2023  # Điều chỉnh năm hiện tại theo năm thực tế
    age = current_year - birth_year
    return f"Chào bạn {full_name}! Bạn đã {age} tuổi."

# Sử dụng hàm greeting()
full_name_input = input("Nhập họ tên của bạn: ")
birth_year_input = int(input("Nhập năm sinh của bạn: "))
result_greeting = greeting(full_name_input, birth_year_input)
print(result_greeting)

def rabbit_count(months):
    initial_rabbits = 1
    rabbits = [initial_rabbits]  # List để lưu số thỏ mỗi tháng
    for _ in range(1, months):
        rabbits.append(rabbits[-1] * 2)  # Mỗi tháng số thỏ gấp đôi
    return rabbits[-1]

# Sử dụng hàm rabbit_count()
months_input = int(input("Nhập số tháng: "))
result_rabbit_count = rabbit_count(months_input)
print(f"Số thỏ trong rừng sau {months_input} tháng là {result_rabbit_count}.")

def count_mark(grades):
    retake_students = sum(mark < 5 for mark in grades)
    total_students = len(grades)
    return retake_students, total_students

# Sử dụng hàm count_mark()
grades_input = [float(x) for x in input("Nhập điểm của sinh viên (cách nhau bởi dấu cách): ").split()]
retake_students, total_students = count_mark(grades_input)
print(f"Số sinh viên học lại là {retake_students} trên tổng số {total_students} sinh viên.")


#15_B
def bmi_show(height, weight):
    # Chuyển đổi chiều cao từ cm sang m
    height_in_meters = height / 100

    # Tính chỉ số BMI
    bmi = weight / (height_in_meters ** 2)

    # Nhận xét dựa vào chỉ số BMI
    if bmi < 18.5:
        return "Gầy, cần tăng cân!"
    elif 18.5 <= bmi < 24.9:
        return "Cân nặng bình thường."
    elif 25 <= bmi < 29.9:
        return "Hơi thừa cân, cần giảm cân!"
    else:
        return "Thừa cân, cần giảm cân!"

# Sử dụng hàm bmi_show()
height_input = float(input("Nhập chiều cao (cm): "))
weight_input = float(input("Nhập cân nặng (kg): "))
result_bmi_show = bmi_show(height_input, weight_input)
print(result_bmi_show)

def cal_point(grades):
    # Tính điểm trung bình hệ 10
    avg_point_10 = sum(grades) / len(grades)

    # Chuyển đổi điểm hệ 10 sang hệ 4
    if 9 <= avg_point_10 <= 10:
        avg_point_4 = 4
    elif 8 <= avg_point_10 < 9:
        avg_point_4 = 3.7
    elif 7 <= avg_point_10 < 8:
        avg_point_4 = 3.3
    elif 6 <= avg_point_10 < 7:
        avg_point_4 = 3
    elif 5 <= avg_point_10 < 6:
        avg_point_4 = 2
    else:
        avg_point_4 = 0

    return avg_point_10, avg_point_4

# Sử dụng hàm cal_point()
grades_input = [float(x) for x in input("Nhập điểm của học sinh (cách nhau bởi dấu cách): ").split()]
result_cal_point = cal_point(grades_input)
print(f"Điểm trung bình hệ 10: {result_cal_point[0]}, Điểm trung bình hệ 4: {result_cal_point[1]}")



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_prime(n):
    primes = [num for num in range(2, n+1) if is_prime(num)]
    return primes

# Sử dụng hàm list_prime()
n_input = int(input("Nhập n để trả về danh sách số nguyên tố từ 1 đến n: "))
result_list_prime = list_prime(n_input)
print(f"Danh sách số nguyên tố từ 1 đến {n_input}: {result_list_prime}")
