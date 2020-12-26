import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv('data/data.csv')
x = data.drop(columns=['result'])
y = data['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# model = KNeighborsClassifier()

# model = SVC(kernel="linear", C=2)

# model = DecisionTreeClassifier()

model = RandomForestClassifier(n_estimators=60, max_depth=3, random_state=1)

model.fit(x_train, y_train)
prediction = model.predict(x_test)

for i in range(len(prediction)):
    if prediction[i] != y_test.values.tolist()[i]:
        print(prediction[i], x_test.values.tolist()[i], y_test.values.tolist()[i])

print(accuracy_score(y_test, prediction))

# joblib.dump(model, 'model.joblib')
# model = joblib.load('model.joblib')
