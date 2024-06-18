import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['K60', 'K61', 'K62', 'K63', 'K64', 'K65']
sv_theo_khoa = [215, 400, 350, 600, 490, 400]
sv_nam_khoa = [200, 320, 265, 420, 300, 190]
sv_nu_khoa = [35, 60, 95, 160, 180, 210]
#Chart 1
plt.figure(figsize = (15, 4))
plt.subplot(1, 2, 1)
plt.plot(labels, sv_nu_khoa, color = 'black', ls = '--', marker = 'o', label = 'Sinh viên Nữ')
plt.plot(labels, sv_nam_khoa, color = 'blue', ls = '--', marker = 'o', label = 'Sinh viên Nam')
plt.plot(labels, sv_theo_khoa, color = 'red', marker = 's', label = 'Tổng số SV')
plt.title('Biểu đồ số lượng SV Nam, Nữ và tổng theo từng khóa', 
          fontdict={'fontname':'Arial', 'fontweight':'bold'})
plt.grid(ls = '--')
plt.legend(loc = 'lower right')

# Chart 2
plt.subplot(1, 2, 2)
e = [0, 0.2, 0.1, 0.3, 0.1, 0]
plt.pie(sv_theo_khoa, 
        labels = labels, 
        autopct = '%.2f %%', 
        startangle = 180,
        wedgeprops = dict(width = 0.6, edgecolor = 'w'), 
        textprops={'fontweight':'bold'}, explode = e, shadow = True)
plt.title('Biểu đồ tỷ lệ SV của từng Khóa', 
          fontdict={'fontname':'Arial', 'fontweight':'bold'})
plt.grid()

plt.grid(axis = 'y', ls = '--')
plt.show()