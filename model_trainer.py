import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
data = pd.read_csv('diabetes.csv')
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train and save models
models = {
    'nb': GaussianNB(),
    'lr': LogisticRegression(max_iter=1000),
    'rf': RandomForestClassifier(),
    'knn': KNeighborsClassifier(),
    'svm': SVC(probability=True),
    'dt': DecisionTreeClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    joblib.dump(model, f'{name}_model.pkl')
