from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# load trained model
model = pickle.load(open("model/kmeans_model.pkl", "rb"))

# load dataset for dashboard stats
df = pd.read_csv("data/Mall_Customers.csv")

total_customers = len(df)
avg_income = df["Annual Income (k$)"].mean()

# cluster meanings
segments = {
0: "Budget Customers",
1: "Young High Spenders",
2: "Regular Customers",
3: "Careful High Income Customers",
4: "Luxury Shoppers"
}

@app.route("/")
def home():
    return render_template(
        "index.html",
        total=total_customers,
        income=round(avg_income,2)
    )

@app.route("/predict", methods=["POST"])
def predict():

    income = int(request.form["income"])
    score = int(request.form["score"])

    data = np.array([[income, score]])

    cluster = model.predict(data)[0]

    result = segments[cluster]

    return render_template(
        "index.html",
        prediction_text=f"Customer Type: {result}",
        total=total_customers,
        income=round(avg_income,2)
    )

if __name__ == "__main__":
    app.run(debug=True)