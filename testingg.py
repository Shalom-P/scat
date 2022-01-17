from scipy import spatial
from sent2vec.vectorizer import Vectorizer

sentences = [
    "puneeth rajkumar died",
    "puneeth rajkumar died",
    "Puneeth Rajkumar Death | Final Salute: Actor Puneeth Rajkumar Paid Last Respects In Karnataka"
]

vectorizer = Vectorizer()
vectorizer.bert(sentences)
vectors_bert = vectorizer.vectors

dist_1 = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
dist_2 = spatial.distance.cosine(vectors_bert[0], vectors_bert[2])
print('dist_1: {0}, dist_2: {1}'.format(dist_1,dist_2))