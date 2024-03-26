import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns

# Set the seaborn style for plots
sns.set()

# Load the Breast Cancer dataset
breast_cancer = load_breast_cancer()

# Create a DataFrame for features
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
X = X[['mean area', 'mean compactness']]  # Select specific features

# Convert the target variable to categorical and one-hot encoded format
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
y = pd.get_dummies(y, drop_first=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Initialize the KNN classifier with 5 neighbors and Euclidean distance metric
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the target values for the test set
y_pred = knn.predict(X_test)

# Plot the test set with true labels and predicted labels
sns.scatterplot(
    x='mean area', y='mean compactness',
    hue='benign', data=X_test.join(y_test, how='outer')
)
plt.scatter(
    X_test['mean area'], X_test['mean compactness'],
    c=y_pred, cmap='coolwarm', alpha=0.7
)

# Compute and display the confusion matrix
confusion_matrix(y_test, y_pred)
