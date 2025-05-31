import pandas as pd
import matplotlib.pyplot as plt

# CSV 읽기
df = pd.read_csv("materials_data.csv")

# 🔹 1. 밀도 분포 히스토그램
plt.figure(figsize=(8, 5))
plt.hist(df["density"].dropna(), bins=20, edgecolor="black")
plt.title("Density Distribution of Li-Fe-O Materials")
plt.xlabel("Density (g/cm³)")
plt.ylabel("Number of Materials")
plt.grid(True)
plt.tight_layout()
plt.show()

# 🔹 2. 상위 10개 물질 막대그래프 (밀도 높은 순)
top10 = df.sort_values(by="density", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top10["formula"], top10["density"])
plt.title("Top 10 Li-Fe-O Materials by Density")
plt.xlabel("Formula")
plt.ylabel("Density (g/cm³)")
plt.xticks(rotation=45)
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
