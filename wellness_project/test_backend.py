from utils import load_model_and_scaler, load_feature_order, preprocess_user_input, predict_cluster, get_cluster_description

# Load model, scaler, and feature order
model, scaler = load_model_and_scaler()
feature_order = load_feature_order()

# Two very different test cases
test_cases = [
    {"eat_out": 1, "food_budget": 2, "sweet_tooth": 9, "hobby_hours": 1},
    {"eat_out": 8, "food_budget": 9, "sweet_tooth": 1, "hobby_hours": 8}
]

for user_input in test_cases:
    processed, used_features = preprocess_user_input(user_input, feature_order, scaler)
    print("\n🧾 Raw input:", user_input)
    print("➡️ Ordered features:", used_features)
    print("➡️ Processed (scaled) input:", processed)

    cluster = predict_cluster(model, processed)
    desc = get_cluster_description(cluster)
    print("⭐ Predicted Cluster:", cluster)
    print("📄 Description:", desc)
