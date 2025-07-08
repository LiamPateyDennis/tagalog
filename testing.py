import pandas as pd
import numpy as np


string = "kain"
list_chars = list(string)

# print(list_chars[0] + "".join(list_chars[1:]))
# print(list_chars[-1])

tag_df = pd.read_csv("Tagalog.csv")

# print(len(tag_df))
# print(tag_df["Verb"][2])
# print(tag_df["Type 1"][2], tag_df["Type 2"][2], tag_df["Type 3"][2])
# # input
# print("What doe it mean?")
# input1 = input()

# output
# print(len(tag_df))
# print(np.random.randint(0, len(tag_df)))
# for i in range(500):
#     if (np.random.randint(0,4)) == 4:
#         print("Fucked")
# tense_frame[2+question_tense][question]

print(tag_df.iloc[2,0])
