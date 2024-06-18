
numbers_str = input("Nhập dãy số (cách nhau bởi dấu cách): ")
numbers = [int(number) for number in numbers_str.split()]

max_value = max(numbers)
min_value = min(numbers)

index_max = numbers.index(max_value)
index_min = numbers.index(min_value)
numbers[index_max], numbers[index_min] = numbers[index_min], numbers[index_max]

with open("dayso2_bai17.txt", "w") as file:
    file.write(" ".join(map(str, numbers)))

print("Đã thực hiện đổi chỗ và lưu vào file dayso2_bai17.txt.")
