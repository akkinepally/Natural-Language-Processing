import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

text = """APJ Abdul kalam came into this world on 15th October 1931, at a time when India was under British 
occupation. He was born to a Tamil Muslim family in Tamil Nadu. His father was a boat owner while his mother was a 
housewife. Furthermore, Kalam had five siblings and was the youngest of the lot. In school, Kalam was an average 
student but was still hardworking and bright. I think this certainly is a great motivation for all the average 
students out there. Being average, you must never ever underestimate yourself and continue doing the hard work. """

corpus = []
sentences = nltk.sent_tokenize(text)
lem = WordNetLemmatizer()

for count in range(len(sentences)):
    sent = re.sub('[^a-zA-Z]', ' ', sentences[count])
    sent = sent.lower()
    sent = sent.split()
    sent = [lem.lemmatize(count) for count in sent if count not in set(stopwords.words('english'))]
    sent = ' '.join(sent)
    corpus.append(sent)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x = cv.fit_transform(corpus).toarray()

print(x)

