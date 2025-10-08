import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")
type_count = df["Type1"].value_counts(ascending=True)
plt.barh(type_count.index, type_count.values, color="#03dffc", edgecolor="black")
plt.title("# of Pokemon by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()
