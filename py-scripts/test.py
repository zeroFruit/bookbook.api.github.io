import sys, codecs

fileNames =  sys.argv

from collections import Counter
from konlpy.tag import Twitter

keywords = []

k = open("dumb.txt")
datak = k.read()
nlpk = Twitter()
dumb_file = nlpk.nouns(datak)

def keywords_extract(filename): 
   f = codecs.open('./reviews/'+ filename,"r", "utf-8")
   data = f.read()

   nlp = Twitter()
   nouns = nlp.nouns(data)

   for i in nouns:
   	if i in dumb:
   		nouns.remove(i)
   		return nouns

   count = Counter(nouns)
   words = count.most_common(40)

   keyword = words[0:3]

   for i in keyword:
   	word_freq_bid = [i[0],i[1],filename[:-4]]
   	keywords.append(word_freq_bid)

   f.close()
   return keywords

for n in range(1, 6):
	keywords_extract(fileNames[int(n)])

print(keywords) 
