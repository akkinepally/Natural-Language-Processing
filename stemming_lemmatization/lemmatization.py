import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

text = """APJ Abdul kalam came into this world on 15th October 1931, at a time when India was under British 
occupation. He was born to a Tamil Muslim family in Tamil Nadu. His father was a boat owner while his mother was a 
housewife. Furthermore, Kalam had five siblings and was the youngest of the lot. In school, Kalam was an average 
student but was still hardworking and bright. I think this certainly is a great motivation for all the average 
students out there. Being average, you must never ever underestimate yourself and continue doing the hard work. """

sentences = nltk.sent_tokenize(text)
stemmer = WordNetLemmatizer()

for word in range(len(sentences)):
    word_tokens = nltk.word_tokenize(sentences[word])
    words = [stemmer.lemmatize(word) for word in word_tokens if word not in set(stopwords.words('english'))]
    sentences[word] = " ".join(words)

print(sentences)