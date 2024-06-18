import matplotlib.pyplot as plt

# Dữ liệu mẫu (thay thế bằng dữ liệu thực tế của bạn)
thanh_pho = ['Ha Noi', 'Vinh', 'Da Nang', 'NhaTrang', 'Ho Chi MInh c', 'Caf m']
nhiet_do_max = [33.45, 32.57, 29.88 , 28.68, 32.06, 31.37]
nhiet_do_mean = [27.71, 26.72,25.52, 26.17, 26.16, 26.73]
nhiet_do_min = [21.68, 22.60, 20.93, 24.50, 23.22, 23.99]

# 1) Vẽ biểu đồ đường nhiệt độ Max của 6 thành phố
plt.figure(figsize=(8, 5))
plt.plot(thanh_pho, nhiet_do_max, marker='o', linestyle='-', color='r')
plt.title('Biểu đồ Nhiệt độ Max của 6 thành phố')
plt.xlabel('Thành phố')
plt.ylabel('Nhiệt độ Max (°C)')
plt.grid(True)
plt.show()

# 2) Vẽ biểu đồ cột nhiệt độ Mean của 6 thành phố
plt.figure(figsize=(8, 5))
plt.bar(thanh_pho, nhiet_do_mean, color='b')
plt.title('Biểu đồ Nhiệt độ Mean của 6 thành phố')
plt.xlabel('Thành phố')
plt.ylabel('Nhiệt độ Mean (°C)')
plt.grid(axis='y')
plt.show()

# 3) Vẽ biểu đồ điểm nhiệt độ Min của 6 thành phố
plt.figure(figsize=(8, 5))
plt.scatter(thanh_pho, nhiet_do_min, color='g', marker='o')
plt.title('Biểu đồ Nhiệt độ Min của 6 thành phố')
plt.xlabel('Thành phố')
plt.ylabel('Nhiệt độ Min (°C)')
plt.grid(True)
plt.show()
