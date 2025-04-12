# -*- coding: utf-8 -*-
"""ML Project1 V2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ayZa6y5OnbBK0xIgOQIr9Dlvq8YMb3qK
"""

# Install necessary libraries
!pip install scikit-learn pandas

# Importing necessary libraries
import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from google.colab import files

# Upload dataset
uploaded = files.upload()

# Load the dataset into a DataFrame
df = pd.read_csv(next(iter(uploaded)))

# Display the first few rows to inspect the data
df.head()

# Drop the 'Unnamed: 0' column if present
df = df.drop(columns=['Unnamed: 0'], errors='ignore')

# Separate features and labels
X = df.drop('Label', axis=1)  # Features
y = df['Label']  # Target variable

# Display the first few rows of the features and target
X.head(), y.head()

# List of categorical and numerical columns
categorical_cols = ['gender', 'BMI_tags']
numerical_cols = ['age', 'weight(kg)', 'height(m)', 'BMR', 'activity_level', 'calories_to_maintain_weight']

# Preprocessing for numerical data
numerical_transformer = StandardScaler()

# Preprocessing for categorical data
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Define the ColumnTransformer to apply the transformations
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_cols),
        ('num', numerical_transformer, numerical_cols)
    ]
)

# Define the model (DecisionTreeClassifier)
model = Pipeline(steps=[
    ('preprocessing', preprocessor),
    ('classifier', DecisionTreeClassifier(random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model's performance on the test data
accuracy = model.score(X_test, y_test)

# Display the accuracy
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model to a file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model has been saved as 'model.pkl'")

# Provide a download link for the saved model
from google.colab import files

files.download('model.pkl')

# ✅ Step 10: Predict and evaluate
from sklearn.metrics import classification_report, accuracy_score
y_pred = model.predict(X_test)
print("🔍 Accuracy Score:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))