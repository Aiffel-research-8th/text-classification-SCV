import os
import pandas as pd

path = "data/kakao"
file_list = os.listdir(path)

conversation = []

for file in file_list:
    with open(os.path.join(path, file)) as f:
        
        content = ""
        for line in f.readlines():
            content += line[4:]
            
        conversation.append(content)

data = pd.DataFrame({
    "conversation": conversation
})

data["idx"] = data.index
data["class"] = "일반 대화"

data = data[["idx", "class", "conversation"]]

length = data["conversation"].apply(len)

bool_index = (50 <= length) and (length <= 300)
print(bool_index)
print(len(data[bool_index]))


# data.to_csv("normal_data.csv", index=False)

# print(data.head())

# train = pd.read_csv("data/train.csv")
# # print(train.head())

# concat = pd.concat([train, data], axis="rows")
# print(concat.head(10))
# concat = concat.sample(frac=1).reset_index(drop=True)
# concat["idx"] = concat.index
# print(concat.head(10))
# print(len(concat))

# concat.to_csv("train3.csv", index=False)