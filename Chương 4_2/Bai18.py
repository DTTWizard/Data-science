import numpy as np

a = np.random.randint(0, 101, size=(12, 12))

# Yêu Cầu 1

print(f"Ma trận a là: \n{a}")
print(f"Kiểu dữ liệu của phần tử trong ma trận: {a.dtype}")
print(f"Kích thước của mảng ma trận: {a.shape}")
print(f"Số phần tử của ma trân: {a.size}")
print(f"Số chiều của mảng ma trận là: {a.ndim}")

# Yêu Cầu 2

main_diagonal = a.diagonal()
print(f"Vector các phần tử nằm trên đường chéo chính:")
print(main_diagonal)
anti_diagonal = np.fliplr(a).diagonal()
print(f"Vector các phần tử nằm trên đường chéo phụ: \n {anti_diagonal}")

# Yêu Cầu 3
x = int(input("Nhập số: "))
# Đếm số lượng phần tử bằng, lớn hơn và nhỏ hơn giá trị x
so_luong_bang_x = np.sum(a == x)
so_luong_lon_hon_x = np.sum(a > x)
so_luong_nho_hon_x = np.sum(a < x)

# In kết quả
print(f"Số lượng phần tử bằng {x}: {so_luong_bang_x}")
print(f"Số lượng phần tử lớn hơn {x}: {so_luong_lon_hon_x}")
print(f"Số lượng phần tử nhỏ hơn {x}: {so_luong_nho_hon_x}")
print  ('Đỗ Trọng Tiến-2121050667')