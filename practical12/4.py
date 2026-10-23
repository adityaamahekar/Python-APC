import matplotlib.pyplot as plt

marks=[45,50,55,60,60,65,70,75,75,80,85,90,90,95,100]

plt.hist(marks,bins=5,color="orange",edgecolor="black")
plt.title("Marks Distrubution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()