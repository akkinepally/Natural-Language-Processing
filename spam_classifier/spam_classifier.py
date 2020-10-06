import nltk
# nltk.download()
import re
import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
lem = WordNetLemmatizer()

email_data = pd.read_csv('email_dataset', sep='\t', names=['label', 'message'])

# preprocessing
corpus = []
for count in range(len(email_data)):
    message = re.sub('[^a-zA-Z]', ' ', email_data['message'][count])
    message = message.lower()
    message = message.split()
    message = [lem.lemmatize(word) for word in message if word not in set(stopwords.words('english'))]
    message = " ".join(message)
    corpus.append(message)

# converting text to vectors
vector = TfidfVectorizer()
x = vector.fit_transform(corpus).toarray()
print(x)

# changing the labels to binary
y = pd.get_dummies(email_data['label'])
y = y.iloc[:, 1].values

# splitting the data
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# model
from sklearn.naive_bayes import MultinomialNB
nb_classifier_model = MultinomialNB().fit(x_train, y_train)


# predict
y_pred = nb_classifier_model.predict(x_test)
print(y_pred)

# confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#accuracy
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, y_pred)
print(score)





