import requests
import pandas as pd

df = pd.read_csv("data/combined.csv")
df.fillna('Bilgi yok', inplace=True)


final_df = []

# loop through the rows and print the dict with column:value
for index, row in df.iterrows():
    final_df.append(row.to_dict())


# print the final list
requests.post(
    "http://localhost:8000/batch_insert",
    json=final_df
)
