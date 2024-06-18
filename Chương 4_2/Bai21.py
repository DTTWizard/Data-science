#1) Đọc dữ liệu lưu trữ trong file Diamonds.txt vào biến kiểu mảng data_diamond, cho biết kích thước, số chiều, kiểu dữ liệu và số phần tử của biến data_diamond

import numpy as np
file_path = 'Diamonds.txt'
data_diamond = np.loadtxt(file_path, delimiter=',')
print("Kích thước của biến data_diamond:", data_diamond.shape)
print("Số chiều của biến data_diamond:", data_diamond.ndim)
print("Kiểu dữ liệu của biến data_diamond:", data_diamond.dtype)
print("Số phần tử của biến data_diamond:", data_diamond.size)
#2Tách mảng data_diamond thành 2 vector: diamond_size và diamond_price lưu trữ trọng lượng và giá bán.

import numpy as np
file_path = 'Diamonds.txt'
data_diamond = np.loadtxt(file_path, delimiter=',')
diamond_size = data_diamond[:, 0] 
diamond_price = data_diamond[:, 1] 
print("Vector diamond_size:", diamond_size)
print("Vector diamond_price:", diamond_price)

#3) Vẽ đồ thị thể hiện mối quan hệ giữa kích thước và giá bán kim cương. Xác định hệ số tương quan tương ứng giữa 2 thông số này.
import numpy as np
import matplotlib.pyplot as plt
file_path = 'Diamonds.txt'
data_diamond = np.loadtxt(file_path, delimiter=',')

diamond_size = data_diamond[:, 0]
diamond_price = data_diamond[:, 1]

plt.scatter(diamond_size, diamond_price, color='blue', marker='o')
plt.title('Mối quan hệ giữa Kích thước và Giá bán kim cương')
plt.xlabel('Kích thước')
plt.ylabel('Giá bán')
plt.grid(True)
plt.show()
correlation_coefficient = np.corrcoef(diamond_size, diamond_price)[0, 1]
print("Hệ số tương quan:", correlation_coefficient)

# 4) Cho biết kích thước và giá trung bình của 50 viên kim cương. Hiển thị giá bán của viên kim cương có trọng lượng 3.01 carat.
import numpy as np

file_path = 'Diamonds.txt'
data_diamond = np.loadtxt(file_path, delimiter=',')

diamond_size = data_diamond[:, 0]
diamond_price = data_diamond[:, 1]

first_50_diamonds_size = diamond_size[:50]
first_50_diamonds_price = diamond_price[:50]

average_size_50_diamonds = np.mean(first_50_diamonds_size)
average_price_50_diamonds = np.mean(first_50_diamonds_price)


print("Kích thước trung bình của 50 viên kim cương:", average_size_50_diamonds)
print("Giá trung bình của 50 viên kim cương:", average_price_50_diamonds)

carat_3_01_price = diamond_price[diamond_size == 3.01]
print("Giá bán của viên kim cương có trọng lượng 3.01 carat:", carat_3_01_price[0])
