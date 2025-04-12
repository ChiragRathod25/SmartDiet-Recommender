# ✅ STEP 1: Import necessary libraries
import joblib
import pandas as pd

# ✅ STEP 2: Load the trained model
clf = joblib.load('diet_model.pkl')
print("\n✅ Model loaded successfully!")

# ✅ STEP 3: Prepare your new input data (new sample to predict)
# Example input data (replace with actual data)
new_data = pd.DataFrame({
    'age': [25],
    'weight(kg)': [70],
    'height(m)': [1.75],
    'gender': ['M'],
    'BMR': [1500],
    'activity_level': [1.7],
    'calories_to_maintain_weight': [2200],
    'BMI_tags': [8]
})

# ✅ STEP 4: Make prediction
prediction = clf.predict(new_data)
print("\n✅ Predicted Diet Type: ", prediction[0])
