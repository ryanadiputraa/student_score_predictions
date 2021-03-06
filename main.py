import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle

data = pd.read_csv('student-mat.csv', sep=';')
data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences', 'traveltime', 'freetime', 'Dalc', 'Walc', 'Medu', 'Fedu']]

# print(data.head())

predict = 'G3'

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

'''  # Train and save model
best = 0
for _ in range(10000):  
  x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
  linear = linear_model.LinearRegression()

  # find the fit line (train model)
  linear.fit(x_train, y_train)
  # test model accuracy
  acc = linear.score(x_test, y_test)    
  if acc > 0.97:
    print('Accuracy : ', acc)


  # save the model
  if acc > best:
    best = acc
    with open('studentmodel.pickle', 'wb') as f:
      pickle.dump(linear, f)
'''

#open and load the model
pickle_in = open('studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)


# Coefficient or Slope (m), in this case its multidimensional
print('Coefficient : \n', linear.coef_)
# y intercept (b)
print('Intercept : \n', linear.intercept_, end='\n\n')

# prediction
predictions = linear.predict(x_test)
  
for x in range(len(predictions)):
  print(predictions[x], x_test[x], y_test[x])


# plotting
second_grade = 'G2'
third_grade = 'G3'
style.use('ggplot')
pyplot.scatter(data[second_grade], data[third_grade])
pyplot.xlabel('Second Grade')
pyplot.ylabel('Third Grade')
pyplot.show()