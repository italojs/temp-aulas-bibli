
from sklearn.naive_bayes import MultinomialNB

goodPayer1 = [0, 1, 1]
goodPayer2 = [0, 0, 1]
goodPayer3 = [0, 0, 0]
badPayer1 =  [1, 1, 0]
badPayer2 =  [1, 0, 0]
badPayer3 =  [1, 1, 0]

data = [goodPayer1, goodPayer2, goodPayer3, 
           badPayer1, badPayer2, badPayer3]

classes = [1, 1, 1, 0, 0, 0]

model = MultinomialNB()
model.fit(data, classes)

data_teste = [1, 1, 0]

prediction = model.predict([data_teste])

print(prediction)