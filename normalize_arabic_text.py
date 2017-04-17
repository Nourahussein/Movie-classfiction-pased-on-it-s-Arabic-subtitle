import re
import string
import sys
import argparse
def normalize_arabic(input_file,output_file):
    file_content = open(input_file).read()
    #normalize arabic text
    file_content = re.sub("[إأآا]", "ا", file_content)
    file_content = re.sub("ى", "ي", file_content)
    file_content = re.sub("ؤ", "ء", file_content)
    file_content = re.sub("ئ", "ء", file_content)
    file_content = re.sub("ة", "ه", file_content)
    file_content = re.sub("گ", "ك", file_content)
    output = open("output.txt", "w")

    output.write(file_content)

    output.close()
    
    return output
normalize_arabic("input.txt", "output.txt")
