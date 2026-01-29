import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

MODEL_VERSION = "v1"

def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X, y)
    os.makedirs("model", exist_ok=True)
    joblib.dump(clf, f"model/iris_clf_{MODEL_VERSION}.pkl")
    print(f"✅ Model v{MODEL_VERSION} trained and saved!")

if __name__ == "__main__":
    train_model()
