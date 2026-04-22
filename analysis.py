import pandas as pd
import matplotlib.pyplot as plt

# قراءة البيانات
data = pd.read_csv("data.csv")

# عرض أول البيانات
print(data.head())

# حساب المتوسط
average_time = data["time_spent"].mean()
print("Average Time Spent:", average_time)

# رسم بياني
# رسم بياني احترافي
avg_by_gender = data.groupby("gender")["time_spent"].mean()

plt.figure(figsize=(8,5))

avg_by_gender.plot(kind="bar", color=["#4CAF50", "#2196F3"])

plt.title("Average Time Spent by Gender", fontsize=14, fontweight="bold")
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Time Spent", fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

plt.savefig("chart.png")  # حفظ الصورة
plt.show()