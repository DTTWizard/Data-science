import pandas as pd
# Đường dẫn đến file Excel
excel_file_path = 'Data_Excercise/excel_Data_Movies.xls'
# Đọc tất cả các sheet từ file Excel vào một dictionary
excel_data = pd.read_excel(excel_file_path, sheet_name=None)
# Gộp các DataFrame từ dictionary thành một DataFrame lớn
merged_dataframe = pd.concat(excel_data.values(), ignore_index=True)
# In ra một số dòng đầu của DataFrame
print(merged_dataframe.head())
