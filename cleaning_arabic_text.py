import re
import string
import sys
import argparse
#arabic diacritics
arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
# list of arabic punctuations which should remove
numbers = '''0123456789'''

arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
english_alphpets ='''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
punctuations_list = arabic_punctuations + english_punctuations +numbers + english_alphpets

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
