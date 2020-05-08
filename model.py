import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

class Model():
    def __init__(self):
        # Load the trained model and TFIDF Vector
        tf1 = pickle.load(open("TFIDF/tfidf_vocab.pickle", 'rb'))
        self.tfid = TfidfVectorizer(stop_words = "english",vocabulary = tf1.vocabulary_)
        self.model = pickle.load(open('Models/pa_clf.sav', 'rb'))
    def transformData(self, newCorpus):
        return self.tfid.fit_transform(newCorpus)
    def predict(self, data):
        return self.model.predict(self.transformData(data))

"""
Example use case for this
myModel = Model()
new_corpus = ["New York City had alerted Monday that 15 patients between 2 and 15 were hospitalized over the past three weeks with the Covid-related syndrome. Most of them tested positive for coronavirus or had positive antibody tests. Some of the children had persistent fever, toxic shock syndrome, and features similar to Kawasaki disease, the state health advisory said. Kawasaki disease causes inflammation in the walls of the arteries and can limit blood flow to the heart. While it's usually treatable and most children recover without serious problems, it can also be deadly. It mainly affects children under 5."]
print(myModel.predict(new_corpus))
"""
