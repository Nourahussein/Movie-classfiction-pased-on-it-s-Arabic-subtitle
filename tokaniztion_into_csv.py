
# coding: utf-8

# In[ ]:

import nltk
import csv
import pandas as pd
#enter your txt file path for input , and csv file for output
def tokanzie_into_csv(input_file,output_file):
  file_content = open(input_file).read()
  tokens = nltk.word_tokenize(file_content)
  df = pd.DataFrame(tokens, columns=["colummn"])
  df.to_csv(output_file, index=False) 

