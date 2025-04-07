import pandas as pd

df = pd.read_csv("organizations-100.csv")

countries = df["Country"].unique()

for country in countries:
    country_df = df[df["Country"] == country]
    country_df.to_csv(f"Country_folder/{country}.csv", index=False)

print("Files created successfully!")