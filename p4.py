
from sklearn.naive_bayes import MultinomialNB
import csv

def get_dataset():
  data = []
  classes = []
  
  with open('./csv/dataset_cat.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if(row["assunto"] == "MachineLearning"):
        data.append([int(row["acessou_pag"]), int(row["acessou_meetup"]), 0, 0, 1, int(row["compartilhou"])])
      elif(row["assunto"] == "DeepLearning"):
        data.append([int(row["acessou_pag"]), int(row["acessou_meetup"]), 0, 1, 0, int(row["compartilhou"])])
      else:
        data.append([int(row["acessou_pag"]), int(row["acessou_meetup"]), 1, 0, 0, int(row["compartilhou"])])
      classes.append(int(row["compareceu"]))

  return data, classes

data, classes = get_dataset()

model = MultinomialNB()
model.fit(data, classes)
data_test = [ 
              [0,0,1,1,0,0],
              [1,1,1,1,0,0],
              [1,0,0,0,0,1]
            ]
classes_test = [0,0,1] 

prediction = model.predict(data_test)

print(prediction)

hits = 0
for p in range(len(prediction)):
    if prediction[p] == classes_test[p]:
        hits = hits+1

print(hits, "/", len(data_test))

accuracy = (hits/len(data_test))*100
print(int(accuracy), "%" )
