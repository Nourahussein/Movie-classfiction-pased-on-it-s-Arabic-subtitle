
# coding: utf-8

# In[ ]:

import nltk
import csv
import pandas as pd
file_content = open("test.txt").read()
tokens = nltk.word_tokenize(file_content)
df = pd.DataFrame(tokens, columns=["colummn"])
cols.remove("coulmn")
df.to_csv('list.csv', index=False)

