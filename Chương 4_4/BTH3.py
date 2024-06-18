import matplotlib.pyplot as plt
import numpy as np

# Data
khoa = ['K60', 'K61', 'K62', 'K63', 'K64', 'K65']
labels = ['Nam', 'Nữ']
y = [215, 400, 345, 600, 490, 400]
y1 = [1714, 736]

# Chart 1
plt.figure(figsize = (15, 4))
plt.subplot(1, 2, 1)
plt.pie(y1, 
        labels = labels, 
        autopct = '%.2f %%', 
        startangle = 90, 
        wedgeprops = dict(edgecolor = 'w'), 
        textprops={'color':'white', 'fontweight':'bold'})
plt.title('Biểu đồ tỷ lệ SV Nam - Nữ của Khoa CNTT', 
          fontdict={'fontname':'Arial', 'fontweight':'bold'})
plt.legend(loc = 'lower right', ncol = 1 )
plt.grid()

#Chart 2
plt.subplot(1, 2, 2)
bars = plt.bar(khoa, y, width = 0.7)
bars[3].set_color('orange')
plt.title('Biểu đồ số lượng SV theo từng khóa', 
          fontdict={'fontname':'Arial', 'fontweight':'bold'})

plt.grid(axis = 'y', ls = '--')
plt.show()