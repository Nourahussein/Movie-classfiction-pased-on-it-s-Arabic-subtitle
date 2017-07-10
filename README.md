# Movie-classfiction-pased-on-it-s-Arabic-subtitle

basic phases 
============


1- getting data:
----------------

* download arabic movies' subtitles from http://subscene.com/
 
2- cleaning data:
-----------------

* Pre-process arabic text (remove diacritics, punctuations and repeating characters).

3-text extraction:
------------------

1-remove stop words

2- stemming using  Khoja Stemmer : http://zeus.cs.pacificu.edu/shereen/research.htm  with command line and connect it with python.


3- caculate the ferquancy of every word in each genre to use it later in claasfiation phase.


4-classification:
-----------------
* classifiy each movie into it's main genres by comparing the most common words in this movie with the  csv file of mean of each 
movie class. and finaly determine the main generis of this movie.


5-training:
-----------

* train the code for each genre and get the result of the mean wight of each word from most common words in each genre.

6-testing:
----------
* testing the code on some movies and calculate the accuracy.
