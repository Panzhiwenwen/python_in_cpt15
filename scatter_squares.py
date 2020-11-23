import matplotlib.pyplot as plt
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Reds,edgecolor='none',s=40)
plt.title("Squares numbers",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')

