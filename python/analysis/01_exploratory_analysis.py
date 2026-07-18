import pandas as pd

df = pd.read_csv("data/cleaned/complaints_cleaned.csv")

print("="*60)
print("BANKING COMPLAINT EXPLORATORY ANALYSIS")
print("="*60)

print("\nTOP 10 PRODUCTS")
print("-"*40)
print(df["Product"].value_counts().head(10))

print("\nTOP 10 COMPANIES")
print("-"*40)
print(df["Company"].value_counts().head(10))

print("\nTOP 10 STATES")
print("-"*40)
print(df["State"].value_counts().head(10))

print("\nSUBMISSION CHANNELS")
print("-"*40)
print(df["Submitted via"].value_counts())

print("\nTOP 10 ISSUES")
print("-"*40)
print(df["Issue"].value_counts().head(10))

print("\nTOP ISSUES FOR CREDIT CARDS")
print("-"*40)

credit_card = df[df["Product"] == "Credit card"]
print(credit_card["Issue"].value_counts().head(10))