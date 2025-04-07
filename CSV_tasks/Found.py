import pandas as pd

df = pd.read_csv("organizations-100.csv")

dates = df["Founded"].unique()

for date in dates:
    date_df = df[df["Founded"] == date]
    date_df.to_csv(f"Found_date/{date}.csv", index=False)

print("Files created successfully!")