import os
import pandas as pd
import numpy as np

path = "data/source"
dirs = ["band", "facebook", "kakao", "nateon"]
# file_list = os.listdir(path)

all_conversation = []

for directory in dirs:
    
    conversation = []
    
    file_list = os.listdir(os.path.join(path, directory))
    
    for file in file_list:

        with open(os.path.join(path, directory, file)) as f:
            
            content = ""
            for line in f.readlines():
                content += line[4:]
                
            conversation.append(content)
            
    conversation = pd.Series(conversation)
    
    length = conversation.apply(len)
    
    index = (50 <= length) & (length <= 300)
    
    conversation = conversation[index]
    print("len", len(conversation))
    all_conversation += conversation[:250].values.tolist()

data = pd.DataFrame({
    "conversation": all_conversation
})

data["idx"] = data.index
data["class"] = "일반 대화"

data = data[["idx", "class", "conversation"]]

print(data.shape)
print(data.head())

data.to_csv("multiple_data.csv", index=False)