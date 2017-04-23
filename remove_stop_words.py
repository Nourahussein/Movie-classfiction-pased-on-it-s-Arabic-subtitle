from nltk.tokenize import word_tokenize
input= open("arabic").read()
stopwords = word_tokenize(input)

file_content = open("newer.txt").read()
words = word_tokenize(file_content)

output = open("team.txt", "w")

for w in words:
    if w not in stopwords:
        output.write(w)
        output.write(" ")

output.close()
