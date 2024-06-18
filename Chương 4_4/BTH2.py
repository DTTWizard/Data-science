import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1990, 2008, 19)
# UK
y1 = np.array([2.8, 2.85, 2.9, 2.75, 2.83, 3.05, 3.1, 1.5, 4, 1.8, 7, 2.2, 6, 3, 3.7, 5.2, 5.5, 2.1, 3.5])
# South Korea
y2 = np.array([2, 2.4, 2.8, 2.85, 2.9, 2.75, 2.83, 3.05, 3.1, 1.5, 4, 1.8, 2.2, 5.6, 3.7, 5.2, 2.1, 3.5, 2.4])
# Autralia
y3 = np.array([0, 1.85, 2.8, 2.85, 2.9, 2.75, 2.83, 3.05, 3.1, 1.5, 1.8, 7, 2.2, 3.7, 4.5, 5.2, 2.1, 3.5, 2.4])
# USA
y4 = np.array([1.1, 1.07, 1.05, 1.03, 1.01, 1.03, 1.14, 1.12, 1.1, 1.4, 1.37, 1.35, 1.41, 1.55, 1.75, 2, 2.4, 2.8, 2.85])

plt.figure(figsize = (8, 4))
plt.plot(x, y1, color = 'red', linestyle = '-', linewidth =1.0, marker = '^', markersize = 7, markerfacecolor='black',alpha=0.6, label = 'UK')
plt.plot(x, y2, color = 'yellow', linestyle = '--', linewidth =1.0, marker = '', markersize = 5, alpha=0.6, label = 'South Korea')
plt.plot(x, y3, color = 'blue', linestyle = '--', linewidth =1.0, marker = '', markersize = 5, alpha=0.6, label = 'Autralia')
plt.plot(x, y4, color = 'black', linestyle = '-', linewidth =1.0, marker = '^', markersize = 7, markerfacecolor='white', alpha=0.6, label = 'USA')
plt.title('Gas Prices over Time 1990 - 2008', fontdict = {'fontweight' : 'bold'})
plt.xlabel('')
plt.ylabel('Dollars ($)', fontdict = {'fontname' :'Comic Sans MS', 'fontweight' : 'bold', 'fontsize' :12})

plt.xlim(1989, 2009)
plt.ylim(0, 8)

plt.xticks(x, rotation = 45)
plt.legend(loc = 4, ncol = 2,)
plt.grid(axis = 'x', color = 'black', linestyle = '--', linewidth = 0.5, alpha=0.5)

plt.show()

           