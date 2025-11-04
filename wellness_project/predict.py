# predict.py
import joblib
import numpy as np
import pandas as pd

def load_model_and_scaler():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    with open("feature_order.txt", "r") as f:
        feature_order = [line.strip() for line in f.readlines()]
    return model, scaler, feature_order

def predict_cluster(eat_out, food_budget, sweet_tooth, hobby_hours):
    model, scaler, feature_order = load_model_and_scaler()
    data = pd.DataFrame([[eat_out, food_budget, sweet_tooth, hobby_hours]], columns=feature_order)
    data_scaled = scaler.transform(data)
    cluster = model.predict(data_scaled)[0]
    return int(cluster)
