import matplotlib.pyplot as plt

x = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,2004, 2005, 2006, 2007, 2008]
y = [3.2, 3.48, 3.6, 4.25, 4.35, 4.4, 3.65, 3.3, 2.7, 3.3, 3.65, 3.3, 3.2, 3.48, 3.9, 4.35, 4.49, 4.5, 5.5]

plt.figure(figsize = (8, 3))

plt.plot(x,
         y,
         color = 'green',
         linestyle = '-.',
         linewidth = 0.5,
         marker = 'd',
         markersize = 5)

plt.title('Biểu đồ giá Gas tại Nhật giai đoạn 1990 - 2008')
plt.xlabel('Thời Gian')
plt.ylabel('Gía Gas (USD)')

plt.xlim(1989, 2009)
plt.ylim(2.5, 6)

plt.xticks(x, rotation = 45)

plt.grid(axis = 'y',
        color = 'black',
        linestyle = ':',
        linewidth = 0.5)
plt.show()

