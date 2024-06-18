import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu từ file CSV
file_path = 'Data_Patient.csv'
df_patient = pd.read_csv(file_path)

# Hiển thị thông tin về dữ liệu và kiểm tra giá trị thiếu
print("Thông tin về dữ liệu:")
print(df_patient.info())

# 2. Xác định cột chứa giá trị khuyết thiếu và vị trí thiếu dữ liệu
missing_values = df_patient.isnull().sum()
columns_with_missing_values = missing_values[missing_values > 0].index
missing_values_positions = df_patient[df_patient[columns_with_missing_values].isnull().any(axis=1)][columns_with_missing_values]

print("\nCác cột chứa giá trị khuyết thiếu:")
print(columns_with_missing_values)
print("\nVị trí thiếu dữ liệu:")
print(missing_values_positions)

# 3. Đề xuất phương án xử lý giá trị thiếu
#    - Trong ví dụ này, chúng ta sẽ xóa các dòng chứa giá trị thiếu. Tùy thuộc vào ngữ cảnh, bạn có thể chọn phương án xử lý khác.
df_patient_no_missing = df_patient.dropna()

# Hiển thị số lượng dòng sau khi xóa giá trị thiếu
print(f"\nSố lượng dòng sau khi xóa giá trị thiếu: {len(df_patient_no_missing)}")

# 4. Phát hiện và xử lý ngoại lai (Outliers)
#    - Trong ví dụ này, chúng ta sẽ xử lý ngoại lai cho cột 'Age' sử dụng phương pháp IQR.
Q1 = df_patient['Age'].quantile(0.25)
Q3 = df_patient['Age'].quantile(0.75)
IQR = Q3 - Q1

outliers_condition = (df_patient['Age'] < Q1 - 1.5 * IQR) | (df_patient['Age'] > Q3 + 1.5 * IQR)
df_patient_no_outliers = df_patient[~outliers_condition]

# Hiển thị số lượng dòng sau khi xử lý ngoại lai
print(f"\nSố lượng dòng sau khi xử lý ngoại lai cho cột 'Age': {len(df_patient_no_outliers)}")

# 5. Vẽ đồ thị dạng cột thể hiện kết quả thống kê số lượng theo từng giá trị khác nhau của thuộc tính Type
type_counts = df_patient['Type'].value_counts()

# Vẽ đồ thị
plt.bar(type_counts.index, type_counts.values, color='skyblue')
plt.title('Số lượng theo từng giá trị của thuộc tính Type')
plt.xlabel('Type')
plt.ylabel('Số lượng')
plt.show()
