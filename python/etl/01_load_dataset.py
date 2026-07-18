import pandas as pd 

df = pd.read_csv("data/raw/complaints_raw.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== COLUMN NAMES ==========")
print(df.columns)

print("\n========== DATASET SHAPE ==========")
print(df.shape)