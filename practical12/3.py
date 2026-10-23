import matplotlib.pyplot as plt

labels=['Python','Java','C++','Javascript']
sizes=[20,45,20,15]
colors=['gold','skyblue','lightgreen','salmon']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Programming language")
plt.show()