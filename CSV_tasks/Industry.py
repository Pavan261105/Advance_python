import pandas as pd

df = pd.read_csv("organizations-100.csv")

industries = df["Industry"].unique()

for industry in industries:
    ind_name = industry.strip()
    ind_name = ind_name.replace("/","_")
    industry_df = df[df["Industry"] == industry]
    industry_df.to_csv(f"Industry/{ind_name}.csv", index=False)

print("Industry-wise files created successfully!")