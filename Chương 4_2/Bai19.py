import pandas as pd
import numpy as np

path = 'Data_Excercise/Diem_2A.txt'
data = np.loadtxt(path, delimiter=',', dtype=np.int8)

dtb_hoc_sinh = np.mean(data, axis=0)


# In kết quả
print("1. Điểm trung bình của từng học sinh trong lớp:")
print(dtb_hoc_sinh)

# Tìm điểm trung bình cao nhất và thấp nhất
max_dtb = np.max(dtb_hoc_sinh)
min_dtb = np.min(dtb_hoc_sinh)

# Lấy bảng điểm của học sinh có ĐTB cao nhất và thấp nhất
hs_max_dtb = data[:, dtb_hoc_sinh == max_dtb]
hs_min_dtb = data[:, dtb_hoc_sinh == min_dtb]

# In kết quả
print(f"\nBảng điểm của học sinh có điểm trung bình cao nhất (ĐTB = {max_dtb}):")
print(hs_max_dtb)

print(f"\nBảng điểm của học sinh có điểm trung bình thấp nhất (ĐTB = {min_dtb}):")
print(hs_min_dtb)

#Yêu cầu 2
dtb_mon_hoc = np.mean(data, axis=0)

# In kết quả
print("1. Điểm trung bình của từng học sinh trong lớp:")
print(dtb_mon_hoc)

# Yêu cầu 3
# 1. Sinh viên có điểm đồng đều nhất và lệch nhất trong lớp
std_per_student = np.std(data, axis=0)
most_consistent_student_index = np.argmin(std_per_student)
most_variable_student_index = np.argmax(std_per_student)

most_consistent_student_scores = data[:, most_consistent_student_index]
most_variable_student_scores = data[:, most_variable_student_index]

# Xác định sinh viên thứ mấy
most_consistent_student_number = most_consistent_student_index + 1
most_variable_student_number = most_variable_student_index + 1

# 2. Môn học có điểm đồng đều nhất và lệch nhất
std_per_subject = np.std(data, axis=1)
most_consistent_subject_index = np.argmin(std_per_subject)
most_variable_subject_index = np.argmax(std_per_subject)

most_consistent_subject_scores = data[most_consistent_subject_index]
most_variable_subject_scores = data[most_variable_subject_index]

# Xác định môn học thứ mấy
most_consistent_subject_number = most_consistent_subject_index + 1
most_variable_subject_number = most_variable_subject_index + 1

# In kết quả
print("1. Sinh viên có điểm đồng đều nhất và lệch nhất trong lớp:")
print(f"Sinh viên có điểm đồng đều nhất (sinh viên thứ {most_consistent_student_number}): {most_consistent_student_scores}")
print(f"Sinh viên có điểm lệch nhất (sinh viên thứ {most_variable_student_number}): {most_variable_student_scores}")

print("\n2. Môn học có điểm đồng đều nhất và lệch nhất:")
print(f"Môn học có điểm đồng đều nhất (môn học thứ {most_consistent_subject_number}): {most_consistent_subject_scores}")
print(f"Môn học có điểm lệch nhất (môn học thứ {most_variable_subject_number}): {most_variable_subject_scores}")