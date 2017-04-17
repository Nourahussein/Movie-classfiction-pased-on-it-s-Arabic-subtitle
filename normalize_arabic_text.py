import re
import string
import sys
import argparse
def normalize_arabic(input_file,output_file):
    file_content = open(input_file).read()
    
    #normalize arabic text by replacing some chrachters
    file_content = re.sub("[إأآا]", "ا", file_content)
    file_content = re.sub("ى", "ي", file_content)
    file_content = re.sub("ؤ", "ء", file_content)
    file_content = re.sub("ئ", "ء", file_content)
    file_content = re.sub("ة", "ه", file_content)
    file_content = re.sub("گ", "ك", file_content)
    
    # remove the arabic diacritics from text
    file_content = re.sub(arabic_diacritics, '', file_content)
    
     # remove repeating charchters
    file_content = re.sub(r'(.)\1+', r'\1',file_content)
    
    #remove punctuations from text
    
    translator = str.maketrans('', '', punctuations_list)
    file_content=file_content.translate(translator)
    
    # writing text to output file 
    output = open(output_file, "w")
    
    output.write(file_content)

    output.close()
    
    return output
# example : normalize_arabic("input.txt", "output.txt")
