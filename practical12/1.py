import matplotlib.pyplot as plt

names = ['A' ,'B', 'C', 'D']
values=[25,40,30,50]

plt.bar(names,values,color='blue')

plt.title("Horizontal Bar chart")

plt.xlabel("Values")

plt.ylabel("Names")
plt.show()