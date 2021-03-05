import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import timeit


data = pd.read_csv('data/data.csv')
x = data.drop(columns=['label'])
# x = data.drop(columns=['changed_files_count', 'changes_methods_count', 'files_to_body_ratio',
#                        'methods_to_body_ratio', 'methods_long', 'methods_complexity',
#                        'methods_parameters', 'added_lines', 'removed_lines', 'label'])
y = data['label']


def try_model(model):
    accuracies = []
    f1_scores = []
    start = timeit.default_timer()
    for i in range(100):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        accuracies.append(accuracy_score(y_test, prediction))
        f1_scores.append(f1_score(y_test, prediction, average=None, labels=['good', 'neutral', 'bad']))
    stop = timeit.default_timer()
    print("{}: [highest {}] [accuracy {}] [f1 {}] [time {}]".format(
        model.__class__.__name__,
        round(max(accuracies), 2),
        round(sum(accuracies) / len(accuracies), 2),
        np.round(sum(f1_scores) / len(f1_scores), 2),
        round(stop - start, 2)))


try_model(KNeighborsClassifier())

try_model(SVC(kernel="linear"))

try_model(DecisionTreeClassifier())

try_model(RandomForestClassifier())  # n_estimators=100, max_depth=10, random_state=1

try_model(ExtraTreesClassifier())

try_model(GradientBoostingClassifier())
