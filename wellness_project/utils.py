# utils.py
import joblib
import numpy as np

def load_model_and_scaler():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

def load_feature_order():
    with open("features.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def preprocess_user_input(user_input, feature_order, scaler):
    data = np.array([[user_input[feat] for feat in feature_order]])
    scaled = scaler.transform(data)
    return scaled, feature_order

def predict_cluster(model, processed):
    return int(model.predict(processed)[0])

# Optional: rule-based layer for sanity correction
def rule_based_cluster(user_input):
    if user_input["food_budget"] >= 8 and user_input["sweet_tooth"] <= 4:
        return 1  # Trendy Eater
    if user_input["sweet_tooth"] >= 8:
        return 2  # Sweet Lover
    if user_input["hobby_hours"] >= 9 and user_input["eat_out"] <= 4:
        return 9  # Passionate Creator
    if user_input["hobby_hours"] >= 8 and user_input["eat_out"] >= 7:
        return 7  # Active Extrovert
    if user_input["eat_out"] >= 8 and user_input["food_budget"] >= 8:
        return 0  # Social Foodie
    if user_input["eat_out"] <= 3 and user_input["hobby_hours"] <= 3:
        return 8  # Minimalist
    if user_input["hobby_hours"] >= 8:
        return 4  # Creative Hobbyist
    if 4 <= user_input["eat_out"] <= 6 and 4 <= user_input["food_budget"] <= 6:
        return 6  # Balanced Persona
    if user_input["hobby_hours"] <= 5 and user_input["eat_out"] <= 3:
        return 5  # Chill Introvert
    return 3  # Default: Dessert Devotee

def get_cluster_description(cluster):
    descriptions = {
        0: "🍕 Social Foodie — You love exploring cafes, dining out, and sharing food experiences with friends.",
        1: "🥗 Trendy Eater — Always chasing the latest food trends and dining aesthetics.",
        2: "🍰 Sweet Lover — Dessert is your love language. You believe there’s always room for one more bite of cake!",
        3: "☕ The Classic Soul, Graceful, balanced, and comforted by the familiar — you find beauty in timeless habits and heartfelt simplicity.",
        4: "🎨 Creative Hobbyist — You unwind by creating — painting, crafting, or designing is your therapy.",
        5: "📚 Chill Introvert — You enjoy peaceful evenings, reading, or watching shows in your cozy space.",
        6: "🧘 Balanced Persona — You balance fun, food, and wellness in perfect harmony.",
        7: "💪 Active Extrovert — Fitness, sports, and social adventures keep your energy high.",
        8: "🌿 Minimalist — You prefer simple joys, mindful living, and calm over chaos.",
        9: "🔥 Passionate Creator — You pour your heart into creative pursuits and spend hours perfecting your craft.",
    }
    return descriptions.get(cluster, "🌟 You’re unique — a mix of many personas!")
