import pandas as pd

#Yêu cầu 1: 
file_path = 'Data_Excercise/Data_Patient.csv'
data_patient = pd.read_csv(file_path)

# Hiển thị thông tin của 10 bệnh nhân đầu tiên
first_10_patients = data_patient.head(10)
print("Thông tin của 10 bệnh nhân đầu tiên:")
print(first_10_patients)
# Hiển thị thông tin của 5 bệnh nhân cuối cùng
last_5_patients = data_patient.tail(5)
print("\nThông tin của 5 bệnh nhân cuối cùng:")
print(last_5_patients)

# Đặt lại tên các cột dữ liệu trong Dataframe 
data_patient.rename(columns= {'id':'Patient code', 
                      'feature_1':'Age', 
                      'feature_2':'Gender', 
                      'feature_3':'Type', 
                      'feature_4':'Blood_pressure', 
                      'feature_5':'Cholesterol', 
                      'feature_6':'Heartbeat', 
                      'feature_7':'Thalassemia', 
                      'feature_8':'Result'}, inplace=True)
data_Patient = data_patient
print(data_Patient.head())

#----------------------------------------------------------------------------
# Yêu cầu 2

# Tuổi của bệnh nhân trẻ nhất và già nhất
youngest_patient_age = data_patient['Age'].min()
oldest_patient_age = data_patient['Age'].max()

# Cholesterol trung bình và độ lệch chuẩn
mean_cholesterol = data_patient['Cholesterol'].mean()
std_dev_cholesterol = data_patient['Cholesterol'].std()

# Số lượng bệnh nhân giới tính nam (Male)
male_patients_count = (data_patient['Gender'] == 'Male').sum()

# Số lượng giá trị khác nhau của thuộc tính Type và giá trị xuất hiện nhiều nhất
type_counts = data_patient['Type'].value_counts()
most_common_type = type_counts.idxmax()
most_common_type_count = type_counts.max()

# Hiển thị kết quả
print(f"Tuổi của bệnh nhân trẻ nhất: {youngest_patient_age}")
print(f"Tuổi của bệnh nhân già nhất: {oldest_patient_age}")
print(f"Cholesterol trung bình: {mean_cholesterol}")
print(f"Độ lệch chuẩn của Cholesterol: {std_dev_cholesterol}")
print(f"Số lượng bệnh nhân giới tính nam (Male): {male_patients_count}")
print(f"Số lượng giá trị khác nhau của thuộc tính Type: {len(type_counts)}")
print(f"Giá trị xuất hiện nhiều nhất của thuộc tính Type là '{most_common_type}' với {most_common_type_count} lần xuất hiện.")

#----------------------------------------------------------------------------------------------------------------
# Yêu cầu 3
# Kiểm tra và hiển thị thông tin về dữ liệu thiếu
missing_data_info = data_patient.isnull().sum()

# Lọc ra những cột có dữ liệu thiếu
columns_with_missing_data = missing_data_info[missing_data_info > 0]

# Hiển thị thông tin
if len(columns_with_missing_data) > 0:
    print("Các cột có chứa missing data và số lượng missing data:")
    for column, missing_count in columns_with_missing_data.items():
        print(f"{column}: {missing_count}")
else:
    print("Không có missing data trong dữ liệu.")

#-----------------------------------------------------------------------------------------------------------------
# Yêu cầu 4
# Chọn thông tin của bệnh nhân có index là 'Patient_100', 'Patient_150', 'Patient_200'
data_yc3 = data_Patient
selected_patients_by_index = data_patient[data_patient['Patient code'].isin(['Patient_100', 'Patient_150', 'Patient_200'])]
# Hiển thị thông tin
print("Thông tin của các bệnh nhân có index: Patient_100, Patient_150, Patient_200:")
print(selected_patients_by_index)

# Chọn thông tin của bệnh nhân ở vị trí 255 đến 260 với các thuộc tính Age, Gender và Result
selected_patients_by_position = data_yc3.loc[255:260, ['Age', 'Gender', 'Result']]

# Hiển thị thông tin
print("\nThông tin của bệnh nhân ở vị trí 255 đến 260 với các thuộc tính Age, Gender và Result:")
print(selected_patients_by_position)

#-----------------------------------------------------------------------------------------------------------------
# Yêu cầu 5
data_yc4 = data_Patient
# Thay đổi giá trị cho thuộc tính Gender

data_yc4.loc[:, 'Gender'] = data_yc4['Gender'].replace({'Male': 0, 'Female': 1})

# Thay đổi giá trị cho thuộc tính Result
data_yc4.loc[:, 'Result'] = data_yc4['Result'].replace({0: 'No', 1: 'Yes'})

# Cập nhật giá trị thuộc tính Thalassemia của bệnh nhân có index 'Patient_05'
data_yc4.loc[data_yc4['Patient code'] == 'Patient_05', 'Thalassemia'] = 4.0

# Hiển thị dữ liệu sau khi thay đổi
print("Dữ liệu sau khi thay đổi thuộc tính Gender và Result:")

print(data_yc4.head())
