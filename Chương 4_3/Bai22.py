import pandas as pd

# Yêu cầu 1
# Đọc dữ liệu từ file CSV
print(f"Yêu cầu 1:")
file_path = 'Data_Excercise/csv_Data_Loan.csv'
data = pd.read_csv(file_path)

print(data.head())

#-----------------------------------------------------------------------------------------------------
# Yêu cầu 2
# Chọn các cột dữ liệu số
print(f"Yêu cầu 2:")
data_number = data.select_dtypes(include=['number'])
# Chọn các cột dữ liệu đối tượng
data_object = data.select_dtypes(include=['object'])

print(f"DataFrame chỉ chứa dữ liệu số (df_number): \n{data_number.head()}")
print(f"DataFrame chỉ chứa dữ liệu đối tượng (df_object): \n{data_object.head()}")

#-----------------------------------------------------------------------------------------------------
# Yêu cầu 3
print(f"Yêu cầu 3:")
# Đọc dữ liệu từ file _Temp.txt
file_path = 'Data_Excercise/Temp.txt'
df = pd.read_csv(file_path, names=['Hà Nội', 'Vinh', 'Đà Nẵng', 'Nha Trang', 'TP Hồ Chí Minh', 'Cà Mau'], sep='\t', header=None)
print(f"{df.head()}")
