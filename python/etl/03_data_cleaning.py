import pandas as pd

print("=" * 60)
print("BANKING COMPLAINT ETL PIPELINE")
print("=" * 60)

# Load dataset
df = pd.read_csv("data/raw/complaints_raw.csv")

print(f"\nOriginal Shape : {df.shape}")

#remove duplicates
duplicates = df.duplicated().sum()

df = df.drop_duplicates() 

print(f"Duplicate Rows Removed : {duplicates}")

#remove tags column 

df = df.drop(columns = ["Tags"] )
print("Removed Column : Tags")  

#convert dates to datetime format 
df["Date received"] = pd.to_datetime(
    df["Date received"],
    errors="coerce" #datetime equivalent of NaN or not a time it puts in that cell 
)

df["Date sent to company"] = pd.to_datetime(
    df["Date sent to company"],
    errors="coerce"
)
print("Date conversion successful and we put not a time at invalid dates") 

print(
    f"Invalid dates in Date received : {df['Date received'].isna().sum()}"
)
print(df[df["Date received"].isna()])

print(
    f"Invalid dates in Date sent to company : {df['Date sent to company'].isna().sum()}"
)

print(df[df["Date sent to company"].isna()])

#save cleaned dataset 
df.to_csv("data/cleaned/complaints_cleaned.csv", index=False) #index is for write row names 
print("Cleaned dataset saved successfully")

print("\n") 
print(f"Cleaned Shape : {df.shape}")

print("\n" + "=" * 60)
print("ETL PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)