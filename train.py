import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import timeit


data = pd.read_csv('data/data.csv')
x = data.drop(columns=['label'])
y = data['label']


def try_model(model):
    accuracies = []
    start = timeit.default_timer()
    for i in range(100):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        accuracies.append(accuracy_score(y_test, prediction))
    stop = timeit.default_timer()
    print("{}: [highest {}] [accuracy {}] [time {}]".format(
        model.__class__.__name__,
        round(max(accuracies), 2),
        round(sum(accuracies) / len(accuracies), 2),
        round(stop - start, 2)))


try_model(KNeighborsClassifier())

try_model(SVC(kernel="linear"))

try_model(DecisionTreeClassifier())

try_model(RandomForestClassifier())  # n_estimators=100, max_depth=10, random_state=1

try_model(ExtraTreesClassifier())

try_model(GradientBoostingClassifier())
