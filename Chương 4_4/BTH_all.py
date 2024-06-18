import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('csv_Data_BMI.csv')

# Yêu cầu 1: Thống kê số lượng nam nữ
gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(12, 5))
# Biểu đồ 1: Biểu đồ hình tròn (pie chart) thể hiện phân phối giới tính
plt.subplot(1, 2, 1)
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(edgecolor='w'), textprops={'color': 'w'})
plt.legend(loc='lower right')
# Biểu đồ 2: Biểu đồ cột thể hiện số lượng nam và nữ
plt.subplot(1, 2, 2)
plt.bar(gender_counts.index, gender_counts.values, width=0.7)
plt.grid(axis='y', ls='--')
plt.suptitle('THỐNG KÊ DỮ LIỆU THEO GIỚI TÍNH TRONG TẬP DỮ LIỆU', fontsize=16, y=1.05)
# Hiển thị cả hai biểu đồ cùng một lúc
plt.show()
# -------------------------------------------------------------------------------------------------------------------------------
# Yêu cầu 2: Thực hiện thống kê số lượng theo chỉ số cơ thể (index) và trực quan hóa kết quả
# Thêm cột BMI và BMI_cata
df['BMI'] = df['Weight_kg'] / (df['Height_cm'] / 100) ** 2
df['BMI_cata'] = pd.cut(df['BMI'], bins=[0, 16, 17, 18.5, 25, 30, float('inf')],
                        labels=['Extremely Weak', 'Weak', 'Normal', 'Overweight', 'Obesity', 'Extremely Obesity'])
# Biểu đồ thống kê trạng thái cơ thể
cata_bmi = df['BMI_cata'].value_counts()

plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.barh(cata_bmi.index, cata_bmi.values)
plt.grid()

plt.subplot(1, 2, 2)
plt.pie(cata_bmi, labels=cata_bmi.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(edgecolor='w'), textprops={'color': 'w'})
plt.suptitle('THỐNG KÊ DỮ LIỆU THEO TRẠNG THÁI CƠ THỂ TRONG TẬP DỮ LIỆU', fontsize=16, y=1.05)
plt.show()
#----------------------------------------------------------------------------------------------
# Yêu cầu 4: Thống kê chỉ số cơ thể theo từng giới tính và trực quan hóa
# Biểu đồ tình trạng cơ thể theo giới tính
plt.figure(figsize=(8, 5))
bmi_categories = df['BMI_cata'].cat.categories
male_counts = df[df['Gender'] == 'Male']['BMI_cata'].value_counts()[bmi_categories].values
female_counts = df[df['Gender'] == 'Female']['BMI_cata'].value_counts()[bmi_categories].values

bar_width = 0.35
index = range(len(bmi_categories))

# Biểu đồ cột thể hiện tình trạng cơ thể theo giới tính
plt.bar(index, male_counts, width=bar_width, label='Male')
plt.bar([i + bar_width for i in index], female_counts, width=bar_width, label='Female')
plt.suptitle('BIỂU ĐỒ THỐNG KÊ TÌNH TRẠNG CƠ THỂ THEO GIỚI TÍNH', fontsize=16, y=1.05)
plt.show()
#--------------------------------------------------------------------------------------------
# Yêu cầu 5: Vẽ biểu đồ thể hiện mối tương quan giữa Height và Weight của 500 người
# Biểu đồ phân tán chiều cao và cân nặng
plt.figure(figsize=(8, 5))
plt.scatter(df['Height_cm'], df['Weight_kg'], alpha=0.5, color='red')
plt.title('Biểu đồ phân tán giữa height và weight')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (Kg)')
plt.suptitle('BIỂU ĐỒ THỂ HIỆN MỐI QUAN HỆ GIỮA CHIỀU CAO VÀ CÂN NẶNG TRONG TẬP DỮ LIỆU', fontsize=16, y=1.05)
plt.show()
