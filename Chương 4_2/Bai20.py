import pandas as pd
import numpy as np

# Yêu cầu 1
path = 'Data_Excercise/Temp.txt'
data_numpy = np.loadtxt(path, delimiter=' ', dtype=np.float64)

print(data_numpy)
print(f"Kích thước biến: {data_numpy.shape}")
print(f"Số chiều của biến: {data_numpy.ndim}")
print(f"Kiểu dữ liệu của các phần tử: {data_numpy.dtype}")
print(f"Số phần tử: {data_numpy.size}")

#-------------------------------------------------------------------------------------
#Yêu cầu 2
nhiet_do_trung_binh_cua_6tp = data_numpy.mean()
print(f"Nhiệt dộ trung bình của 6 thành phố là: {nhiet_do_trung_binh_cua_6tp}")

#--------------------------------------------------------------------------------------
#Yêu cầu 3
for i in range(0, data_numpy.shape[1]):
    print(f"Nhiệt độ TB{i}: {data_numpy[:, i].mean()}")

# Tên các thành phố
cities = ['Hà Nội', 'Vinh', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh', 'Cà Mau']

# Duyệt qua từng thành phố
for i, city in enumerate(cities):
    # Lấy dữ liệu nhiệt độ của thành phố tương ứng
    temperatures = data_numpy[:, i]
    
    # Tìm nhiệt độ cao nhất, thấp nhất, và trung bình
    max_temp = np.max(temperatures)
    min_temp = np.min(temperatures)
    avg_temp = np.mean(temperatures)
    
    # Hiển thị kết quả cho từng thành phố
    print(f"Thành phố: {city}")
    print(f"Nhiệt độ cao nhất: {max_temp:.2f}")
    print(f"Nhiệt độ thấp nhất: {min_temp:.2f}")
    print(f"Nhiệt độ trung bình: {avg_temp:.2f}\n")