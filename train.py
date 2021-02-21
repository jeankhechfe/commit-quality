import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# import joblib

data = pd.read_csv('data/data.csv')
x = data.drop(columns=['label'])
y = data['label']


def try_model(model):
    accuracy = 0
    for i in range(100):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        accuracy += accuracy_score(y_test, prediction)
    return accuracy / 100


m1 = KNeighborsClassifier()
print("KNeighborsClassifier:", try_model(m1))

m2 = SVC(kernel="linear")
print("SVC:", try_model(m2))

m3 = DecisionTreeClassifier()
print("DecisionTreeClassifier:", try_model(m3))

m4 = RandomForestClassifier()  # n_estimators=100, max_depth=10, random_state=1
print("RandomForestClassifier:", try_model(m4))

# for i in range(len(prediction)):
#     if prediction[i] != y_test.values.tolist()[i]:
#         print(prediction[i], x_test.values.tolist()[i], y_test.values.tolist()[i])


# joblib.dump(model, 'model.joblib')
# model = joblib.load('model.joblib')
