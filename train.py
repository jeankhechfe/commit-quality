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

UNEQUAL_LABELS = 0
EQUAL_LABELS = 1


def shuffle_and_cut_extra(data):
    good = data[data.label == 'good']
    neutral = data[data.label == 'neutral']
    bad = data[data.label == 'bad']
    good = good.sample(frac=1)
    neutral = neutral.sample(frac=1)
    bad = bad.sample(frac=1)
    shortest_length = min(len(good), len(neutral), len(bad))
    good_shrunk = good[:shortest_length]
    neutral_shrunk = neutral[:shortest_length]
    bad_shrunk = bad[:shortest_length]
    data = pd.concat([good_shrunk, neutral_shrunk, bad_shrunk])
    data = data.sample(frac=1)
    features = data.drop(columns=['label'])
    labels = data['label']
    return features, labels


def get_xy(file_name, labels_numbers):
    data = pd.read_csv(file_name)
    features = data.drop(columns=['label'])
    labels = data['label']
    if labels_numbers == UNEQUAL_LABELS:
        return features, labels
    return shuffle_and_cut_extra(data)


x, y = get_xy('data/data.csv', EQUAL_LABELS)


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

try_model(RandomForestClassifier())

try_model(ExtraTreesClassifier())

try_model(GradientBoostingClassifier())
