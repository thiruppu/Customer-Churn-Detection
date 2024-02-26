import matplotlib.pyplot as plt

# x axis values
x = [0,40,50,60,65,70]
# corresponding y axis values
y = [30,170,300,500,575,700]

# plotting the points
plt.plot(x, y, color='green', linestyle='solid', linewidth = 3,
		marker='', markerfacecolor='green', markersize=9)

# setting x and y axis range
plt.ylim(0,1000)
plt.xlim(0,100)

# naming the x axis
plt.xlabel('Index of Page')
# naming the y axis
plt.ylabel('Request of queueing Delay')

# giving a title to my graph
plt.title('Best effort queueing')
plt.grid()
# function to show the plot
plt.show()
