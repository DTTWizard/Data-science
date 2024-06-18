class Person:
    def __init__(self, name="Your Name", year=2000, height=170, weight=60):
        self.name = name
        self.year = year
        self.height = height
        self.weight = weight

    def greeting(self):
        print(f"Thông tin của {self.name}:")
        print(f"Năm sinh: {self.year}")
        print(f"Chiều cao: {self.height} cm")
        print(f"Cân nặng: {self.weight} kg")

    def bmi(self):
        # Chuyển đổi chiều cao từ cm sang m
        height_in_meters = self.height / 100

        # Tính chỉ số BMI
        bmi_value = self.weight / (height_in_meters ** 2)
        return bmi_value

# Nhập liệu từ bàn phím để tạo đối tượng Person
name_input = input("Nhập họ tên của bạn: ")
year_input = int(input("Nhập năm sinh của bạn: "))
height_input = float(input("Nhập chiều cao của bạn (cm): "))
weight_input = float(input("Nhập cân nặng của bạn (kg): "))

# Tạo đối tượng Person với thông tin nhập từ bàn phím
person_from_input = Person(name_input, year_input, height_input, weight_input)

# Hiển thị thông tin và chỉ số BMI của đối tượng
person_from_input.greeting()
bmi_value = person_from_input.bmi()
print(f"Chỉ số BMI của {person_from_input.name}: {bmi_value}")
