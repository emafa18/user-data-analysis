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
data.groupby("gender")["time_spent"].mean().plot(kind="bar")
plt.title("Average Time Spent by Gender")
plt.ylabel("Time")
plt.show()