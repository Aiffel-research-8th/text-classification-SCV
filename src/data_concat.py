import pandas as pd

data = pd.read_csv("data/multiple_data.csv")

print(data.head())

train = pd.read_csv("data/train.csv")

concat = pd.concat([train, data], axis="rows")
print(concat.head(10))
concat = concat.sample(frac=1).reset_index(drop=True)
concat["idx"] = concat.index
print(concat.head(10))
print(len(concat))

concat.to_csv("train4.csv", index=False)