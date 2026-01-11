from sklearn.svm import SVC

def train_classifier(X, y):
    clf = SVC(kernel="linear")
    clf.fit(X, y)
    return clf
