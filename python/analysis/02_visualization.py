import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/complaints_cleaned.csv")

product_counts = df["Product"].value_counts().head(10)
plt.figure(figsize=(10, 6)) #eidth height 
product_counts.plot(kind="bar") #line pie hist scatter 
plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Count")
plt.xticks(rotation=45) #it rotates x axis labels 
plt.tight_layout() #automatic adjust spacings so labels dont overlap 
plt.show()


company_counts = df["Company"].value_counts().head(10)

plt.figure(figsize=(12,6))

company_counts.plot(kind="bar")

plt.title("Top 10 Companies by Complaints")

plt.xticks(rotation=75)

plt.tight_layout()

plt.show()

state_counts = df["State"].value_counts().head(10)

plt.figure(figsize=(10,6))

state_counts.plot(kind="bar")

plt.title("Top 10 States")

plt.tight_layout()

plt.show()

channel_counts = df["Submitted via"].value_counts()

plt.figure(figsize=(8,8))

channel_counts.plot(kind="pie", autopct="%1.1f%%")
# autopct means show percent there with 1 decimal place 
# ie 90.3 instead of 90.34543 if u want 2 dec then %1.2f%% last la 2 %%
plt.ylabel("")

plt.title("Complaint Submission Channels")

plt.show()