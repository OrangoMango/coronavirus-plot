import matplotlib.pyplot as plt

y = [1]
for x in range(10):
	y.append(y[x]*2)
	
x = [x for x in range(len(y))]

plt.plot(x, y, "--ko", label="Coronavirus", color="red")
plt.plot([0,10], [560,0], label="Money", color="green")

plt.title("Coronavirus death")
plt.xlabel("time")
plt.ylabel("death/euro")
plt.legend()

plt.show()