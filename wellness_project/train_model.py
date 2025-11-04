# train_model.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

# Generate synthetic data for 10 distinct personas
data = pd.DataFrame([
    # 0: Social Foodie
    *[{"eat_out": 9, "food_budget": 9, "sweet_tooth": 5, "hobby_hours": 3} for _ in range(10)],
    # 1: Trendy Eater
    *[{"eat_out": 8, "food_budget": 8, "sweet_tooth": 4, "hobby_hours": 4} for _ in range(10)],
    # 2: Sweet Lover
    *[{"eat_out": 3, "food_budget": 4, "sweet_tooth": 10, "hobby_hours": 2} for _ in range(10)],
    # 3: Dessert Devotee
    *[{"eat_out": 2, "food_budget": 3, "sweet_tooth": 9, "hobby_hours": 1} for _ in range(10)],
    # 4: Creative Hobbyist
    *[{"eat_out": 3, "food_budget": 4, "sweet_tooth": 4, "hobby_hours": 9} for _ in range(10)],
    # 5: Chill Introvert
    *[{"eat_out": 2, "food_budget": 3, "sweet_tooth": 3, "hobby_hours": 5} for _ in range(10)],
    # 6: Balanced Persona
    *[{"eat_out": 5, "food_budget": 5, "sweet_tooth": 5, "hobby_hours": 5} for _ in range(10)],
    # 7: Active Extrovert
    *[{"eat_out": 8, "food_budget": 8, "sweet_tooth": 4, "hobby_hours": 9} for _ in range(10)],
    # 8: Minimalist
    *[{"eat_out": 1, "food_budget": 2, "sweet_tooth": 2, "hobby_hours": 2} for _ in range(10)],
    # 9: Passionate Creator
    *[{"eat_out": 4, "food_budget": 6, "sweet_tooth": 5, "hobby_hours": 10} for _ in range(10)],
])

# Scale and train
features = ["eat_out", "food_budget", "sweet_tooth", "hobby_hours"]
scaler = StandardScaler()
scaled = scaler.fit_transform(data[features])

model = KMeans(n_clusters=10, random_state=42, n_init=10)
model.fit(scaled)

# Save
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

with open("features.txt", "w") as f:
    for feat in features:
        f.write(feat + "\n")

print("✅ Model trained and saved with 10 clusters.")
