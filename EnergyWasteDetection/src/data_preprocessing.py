import pandas as pd

df = pd.read_csv("data/energydata_complete.csv")

print("Original Shape:", df.shape)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (if any)
df.fillna(method="ffill", inplace=True)

print("After Cleaning:", df.shape)

df.to_csv("data/energydata_cleaned.csv", index=False)
print("✅ Preprocessing Complete — cleaned file saved.")
