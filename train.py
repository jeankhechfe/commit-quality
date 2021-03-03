import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import timeit


data = pd.read_csv('data/data.csv')
x = data.drop(columns=['label'])
y = data['label']

iterations = 100
print("Iterations: [{}]".format(iterations))


def try_model(model):
    start = timeit.default_timer()
    total_accuracy = 0
    highest = 0
    for i in range(iterations):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        accuracy = accuracy_score(y_test, prediction)
        total_accuracy += accuracy
        if highest < accuracy:
            highest = accuracy
    stop = timeit.default_timer()
    print("{}: [highest {}] [accuracy {}] [time {}]".format(
        model.__class__.__name__,
        round(highest, 2),
        round(total_accuracy / iterations, 2),
        round(stop - start, 2)))


try_model(KNeighborsClassifier())

try_model(SVC(kernel="linear"))

try_model(DecisionTreeClassifier())

try_model(RandomForestClassifier())  # n_estimators=100, max_depth=10, random_state=1

try_model(ExtraTreesClassifier())

