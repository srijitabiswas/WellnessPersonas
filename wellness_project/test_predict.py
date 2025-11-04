# test_predict.py
from predict import predict_cluster

# Example input values
result = predict_cluster(eat_out=3, food_budget=200, sweet_tooth=4, hobby_hours=10)
print("Predicted Cluster:", result)
