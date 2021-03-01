import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score
import timeit

# import joblib

data = pd.read_csv('data/data.csv')
x = data.drop(columns=['label'])
y = data['label']

iterations = 100
print("Iterations: [{}]".format(iterations))


def try_model(model):
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
    return [round(highest, 2), round(total_accuracy / iterations, 2)]


start = timeit.default_timer()
m1 = KNeighborsClassifier()
results = try_model(m1)
stop = timeit.default_timer()
print("KNeighborsClassifier: [highest {}] [accuracy {}] [time {}]".format(results[0], results[1],
                                                                             round(stop - start, 2)))

start = timeit.default_timer()
m2 = SVC(kernel="linear")
results = try_model(m2)
stop = timeit.default_timer()
print("SVC (linear): [highest {}] [accuracy {}] [time {}]".format(results[0], results[1], round(stop - start, 2)))


start = timeit.default_timer()
m3 = DecisionTreeClassifier()
results = try_model(m3)
stop = timeit.default_timer()
print("DecisionTreeClassifier: [highest {}] [accuracy {}] [time {}]".format(results[0], results[1],
                                                                            round(stop - start, 2)))

start = timeit.default_timer()
m4 = RandomForestClassifier()  # n_estimators=100, max_depth=10, random_state=1
results = try_model(m4)
stop = timeit.default_timer()
print("RandomForestClassifier: [highest {}] [accuracy {}] [time {}]".format(results[0], results[1],
                                                                            round(stop - start, 2)))

start = timeit.default_timer()
m4 = ExtraTreesClassifier()
results = try_model(m4)
stop = timeit.default_timer()
print("ExtraTreesClassifier: [highest {}] [accuracy {}] [time {}]".format(results[0], results[1],
                                                                            round(stop - start, 2)))


# x_trn, x_tst, y_trn, y_tst = train_test_split(x, y, test_size=0.2)
# m.fit(x_trn, y_trn)
# pred = m.predict(x_tst)
# acc = accuracy_score(y_tst, pred)
# print(acc)
# for i in range(1, 21):
#     nof = [1, 0, 1, 1, 1, 1, 1, 1, 3, 0, -1, -1, 1, 1, 1, i*10]
#     print(i, m.predict([nof]))

# for i in range(len(prediction)):
#     if prediction[i] != y_test.values.tolist()[i]:
#         print(prediction[i], x_test.values.tolist()[i], y_test.values.tolist()[i])


# joblib.dump(model, 'model.joblib')
# model = joblib.load('model.joblib')
