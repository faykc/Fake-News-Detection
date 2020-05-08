import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Testing phase
tf1 = pickle.load(open("TFIDF/tfidf_vocab.pickle", 'rb'))

# Create new tfidfVectorizer with old vocabulary
tf1_new = TfidfVectorizer(stop_words = "english",vocabulary = tf1.vocabulary_)

new_corpus = ["New York City had alerted Monday that 15 patients between 2 and 15 were hospitalized over the past three weeks with the Covid-related syndrome. Most of them tested positive for coronavirus or had positive antibody tests. Some of the children had persistent fever, toxic shock syndrome, and features similar to Kawasaki disease, the state health advisory said. Kawasaki disease causes inflammation in the walls of the arteries and can limit blood flow to the heart. While it's usually treatable and most children recover without serious problems, it can also be deadly. It mainly affects children under 5."]

X_tf1 = tf1_new.fit_transform(new_corpus)

model = pickle.load(open('Models/pa_clf.sav', 'rb'))

print(model.predict(X_tf1))
