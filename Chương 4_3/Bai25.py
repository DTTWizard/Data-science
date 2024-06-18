import pandas as pd
import matplotlib.pyplot as plt
#Yêu câu 1
# Đọc dữ liệu từ file CSV và sử dụng cột 'id' làm chỉ số (index_col)
file_path = 'Data_Excercise/Data_Patient.csv'
df_patient = pd.read_csv(file_path, index_col='id')

# Đặt lại tên các cột dữ liệu
df_patient = df_patient.rename(columns={
    'feature_1': 'Age',
    'feature_2': 'Gender',
    'feature_3': 'Type',
    'feature_4': 'Blood_pressure',
    'feature_5': 'Cholesterol',
    'feature_6': 'Heartbeat',
    'feature_7': 'Thalassemia',
    'feature_8': 'Result'
})
# Hiển thị một số dòng đầu của DataFrame sau khi đổi tên cột
print(df_patient.head())

#------------------------------------------------------------------------------------
# Yêu cầu 2
# Lọc dữ liệu thành các DataFrame
df_male = df_patient[df_patient['Gender'] == 'Male']
df_female = df_patient[df_patient['Gender'] == 'Female']
df_no = df_patient[df_patient['Result'] == 0]
df_yes = df_patient[df_patient['Result'] == 1]

# Hiển thị số lượng bệnh nhân trong mỗi DataFrame
print(f"Số lượng bệnh nhân Nam: {len(df_male)}")
print(f"Số lượng bệnh nhân Nữ: {len(df_female)}")
print(f"Số lượng bệnh nhân không bị bệnh đau tim: {len(df_no)}")
print(f"Số lượng bệnh nhân bị bệnh đau tim: {len(df_yes)}")


# Yêu cầu 3

# Yêu cầu 3.1: Những người bị mắc bệnh đau tim và trên 70 tuổi
condition_1 = (df_patient['Heart Disease'] == 'Yes') & (df_patient['Age'] > 70)
result_1 = df_patient[condition_1]

# Yêu cầu 3.2: Người có giới tính Female, có huyết áp trên 170 mmHg nhưng không bị bệnh đau tim
condition_2 = (df_patient['Gender'] == 'Female') & (df_patient['Blood Pressure'] > 170) & (df_patient['Heart Disease'] == 'No')
result_2 = df_patient[condition_2]

# Yêu cầu 3.3: Những người có triệu chứng đau ngực là Typical angina, giới tính Male và bị bệnh đau tim
condition_3 = (df_patient['Chest Pain'] == 'Typical angina') & (df_patient['Gender'] == 'Male') & (df_patient['Heart Disease'] == 'Yes')
result_3 = df_patient[condition_3]

# Hiển thị kết quả
print("Yêu cầu 1:")
print(result_1)

print("\nYêu cầu 2:")
print(result_2)

print("\nYêu cầu 3:")
print(result_3)
#Yêu cầu 4

blood_pressure_min = df_patient['Blood_pressure'].min()
blood_pressure_max = df_patient['Blood_pressure'].max()
blood_pressure_mean = df_patient['Blood_pressure'].mean()
blood_pressure_median = df_patient['Blood_pressure'].median()
blood_pressure_std = df_patient['Blood_pressure'].std()

print("Chỉ số huyết áp:")
print(f"Thấp nhất: {blood_pressure_min}")
print(f"Cao nhất: {blood_pressure_max}")
print(f"Trung bình: {blood_pressure_mean}")
print(f"Trung vị: {blood_pressure_median}")
print(f"Độ lệch chuẩn: {blood_pressure_std}")

heartbeat_min = df_patient['Heartbeat'].min()

print("\nChỉ số nhịp tim:")
print(f"Thấp nhất: {heartbeat_min}")

#Yêu cầu 5
# 1. Số giá trị khác nhau của thuộc tính Type
unique_type_count = df_patient['Type'].nunique()

# Hiển thị kết quả
print("1. Số giá trị khác nhau của thuộc tính Type:", unique_type_count)

# 2. Vẽ đồ thị dạng cột thể hiện kết quả thống kê số lượng theo từng giá trị khác nhau của thuộc tính Type
type_counts = df_patient['Type'].value_counts()

# Vẽ đồ thị
plt.bar(type_counts.index, type_counts.values, color='skyblue')
plt.title('Số lượng theo từng giá trị của thuộc tính Type')
plt.xlabel('Type')
plt.ylabel('Số lượng')
plt.show()