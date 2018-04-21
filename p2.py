
from sklearn.naive_bayes import MultinomialNB

data = [ [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
            [1, 1, 0],
            [1, 0, 0],
            [1, 1, 0]
          ]

classes = [1, 1, 1, 0, 0, 0]


model = MultinomialNB()
model.fit(data, classes)

data_test = [ 
              [1, 1, 0],
              [1, 0, 0],
              [1, 1, 1]
            ]
classes_test = [0, 0, 1] 

prediction = model.predict(data_test)

hits = 0

for p in range(len(prediction)):
    if prediction[p] == classes_test[p] :
        hits = hits+1

print(hits, "/", len(data_test))

accuracy = (hits/len(data_test))*100
print(int(accuracy), "%" )
