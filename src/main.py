import numpy as np
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", 100)

df1 = pd.read_csv("data/depremzedeler.csv")
df2 = pd.read_csv("data/version_4_convertcsv_-_Sheet1.csv")

df = pd.concat([df2, df1], sort=False)
df.fillna(value=np.nan, inplace=True)

df.to_csv("data/combined.csv", index=False)
