import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

font_family = "JetBrains Mono"

plt.title(
    "Class size",
    fontsize=25,
    family=font_family,
    fontweight="bold",
    color="#2d4cfc",
)

plt.xlabel("Year", fontsize=20, family=font_family, fontweight="bold", color="#2dbefc")

plt.ylabel(
    "Students", fontsize=20, family=font_family, fontweight="bold", color="#2dbefc"
)

plt.tick_params(axis="both", colors="#0062ff")

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)

plt.subplots_adjust(bottom=0.175, left=0.14)

plt.show()
