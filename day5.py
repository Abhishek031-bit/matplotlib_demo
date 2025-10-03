import matplotlib.pyplot as plt
import numpy as np

categories = ["Grains", "Fruits", "Vegetables", "Protein", "Dairy", "Sweets"]
values = np.array([4, 3, 2, 5, 3, 1])

plt.bar(categories, values, color="indigo")
# plt.barh(categories, values, color="indigo")

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")


plt.show()
