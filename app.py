from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Extract user input
            input_data = {
                'age': int(request.form['age']),
                'weight(kg)': float(request.form['weight']),
                'height(m)': float(request.form['height']),
                'gender': request.form['gender'],
                'BMI': float(request.form['bmi']),
                'BMR': float(request.form['bmr']),
                'activity_level': float(request.form['activity']),
                'calories_to_maintain_weight': float(request.form['calories']),
                'BMI_tags': int(request.form['bmi_tag'])
            }

            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)[0]

            return render_template("index.html", prediction=f"Predicted Diet Type: {prediction}")
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {str(e)}")

    return render_template("index.html", prediction=None)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # fallback to 5000 for local dev
    app.run(debug=False, host="0.0.0.0", port=port)
