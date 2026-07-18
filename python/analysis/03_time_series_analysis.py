import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/complaints_cleaned.csv")

df["Date received"] = pd.to_datetime(df["Date received"], errors="coerce")
#when we saved to excel the date again become text

df["Year"] = df["Date received"].dt.year
df["Month"] = df["Date received"].dt.month
df["Day"] = df["Date received"].dt.day

year_counts = df["Year"].value_counts().sort_index()
#value count sort by frequency na so here by sortindex we will sort by year

plt.figure(figsize=(10, 6))

year_counts.plot(kind="line", marker="o")
#with markers o────o────o without markers ────── u can use other too like * 
plt.title("Banking Complaints Over Years")
plt.xlabel("Year")
plt.ylabel("No of complaints")
plt.grid(True)
plt.tight_layout() 
plt.show()




month_counts = df["Month"].value_counts().sort_index()
plt.figure(figsize=(10, 6))

month_counts.plot(kind="line", marker="*")
#with markers o────o────o without markers ────── u can use other too like * 
plt.title("Banking Complaints By Months")
plt.xlabel("Months")
plt.ylabel("No of complaints")
plt.grid(True)
plt.tight_layout() 
plt.show()
