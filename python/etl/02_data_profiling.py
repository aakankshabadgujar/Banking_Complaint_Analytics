import pandas as pd 

df = pd.read_csv("data/raw/complaints_raw.csv")

print("="*60)
print("DATASET SHAPE")
print("="*60)
print(df.shape)

print("\n")

print("="*60)
print("MISSING VALUES")
print("="*60)
print(df.isnull().sum())

print("\n")

print("="*60)
print("DUPLICATE RECORDS")
print("="*60)
print(df.duplicated().sum())

print("\n")

print("="*60)
print("PRODUCTS")
print("="*60)
print(df["Product"].value_counts())

print("\n")

print("="*60)
print("TOP 10 STATES")
print("="*60)
print(df["State"].value_counts().head(10))


print("\n")

print("="*60)
print("TOP 10 COMPANIES")
print("="*60)
print(df["Company"].value_counts().head(10))


print("\n")

print("="*60)
print("SUBMITTED VIA")
print("="*60)
print(df["Submitted via"].value_counts().head(10)) 



print("\n")

print("="*60)
print("DATASET DESCRIBED")
print("="*60)
print(df.describe()) 

