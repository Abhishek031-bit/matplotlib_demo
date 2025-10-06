import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10, color="lightgreen", edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("# of Students")

plt.show()
