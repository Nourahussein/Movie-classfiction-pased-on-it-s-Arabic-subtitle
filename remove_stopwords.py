from nltk.corpus import stopwords
stop = set(stopwords.words('arabic'))
def remove_stop(input_file,output_file):
    file_content = open(input_file).read()
    print ([i for i in file_content.split() if i not in stop])

    #writing into file
    output = open(output_file, "w")
    
    output.write(file_content)

    output.close()
    
    return output
#example :remove_stop("output.txt", "output_final.txt")
