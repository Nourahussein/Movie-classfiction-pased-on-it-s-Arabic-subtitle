import nltk
import os
import re
#java_path = "/usr/bin/java"
#os.environ['JAVAHOME'] = java_path
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-oracle"
#from nltk.tag.stanford import POSTagger
from nltk import pos_tag
from nltk import word_tokenize
from nltk.tag.stanford import StanfordTagger
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tag.stanford import StanfordNERTagger
path_to_model= '/home/noura/stanford-postagger-full-2016-10-31/models/arabic.tagger'
path_to_jar = '/home/noura/stanford-postagger/stanford-postagger.jar'
#artagger.java_options='-mx4096m'
artagger = StanfordPOSTagger(path_to_model, path_to_jar, encoding='utf8')
artagger._SEPARATOR = '/'
tagged_sent = artagger.tag(word_tokenize(u'ممتاز و جيد لطيف أشياء أفعال وهذا نص للتأكد فقط لا غير أنا تسلقت شجرة'))
print(tagged_sent)
