# 💪 Wellness Personas of SNU

Welcome to **Wellness Personas of SNU**, an interactive web app that uncovers your lifestyle persona through a blend of **data-driven insights** and **human-centered design**.  
Built by **Prakriti**, **Sresthita**, and **Srijita**, this app helps you explore your wellness style based on your daily habits and preferences.

🔗 **Live App:** [https://wellnesspersonas-cthr6lsavffhyqmycxlyko.streamlit.app/](https://wellnesspersonas-cthr6lsavffhyqmycxlyko.streamlit.app/)

---

## 🌟 Project Overview
This project combines **Machine Learning (KMeans Clustering)** with a beautifully designed **Streamlit interface** to group users into unique lifestyle personas.  

By answering a few quick questions about your habits (like how often you eat out, your food budget, or your hobbies), you’ll discover which persona best represents your lifestyle and wellness approach.  

Each persona reflects a distinct identity — from the calm **Classic Soul ☕** to the energetic **Active Extrovert 💪** — helping students understand themselves better and embrace balanced living.

---

## 🧠 Personas (Clusters)
| Cluster | Persona | Description |
|:--:|:--|:--|
| 0 | 🍕 **Social Foodie** | Loves exploring cafes, dining out, and sharing food experiences with friends. |
| 1 | 🥗 **Trendy Eater** | Follows the latest food trends and enjoys aesthetic dining. |
| 2 | 🍰 **Sweet Lover** | Dessert is your love language — life is sweeter with cake! |
| 3 | ☕ **Classic Soul** | Graceful, balanced, and comforted by the familiar — finds beauty in timeless simplicity. |
| 4 | 🎨 **Creative Hobbyist** | Expresses emotions through art, design, or creative crafts. |
| 5 | 📚 **Chill Introvert** | Finds joy in peace, books, and cozy solitude. |
| 6 | 🧘 **Balanced Persona** | Lives in perfect harmony between fun, food, and wellness. |
| 7 | 💪 **Active Extrovert** | Thrives in sports, fitness, and social adventures. |
| 8 | 🌿 **Minimalist** | Prefers simple joys, mindfulness, and calm over chaos. |
| 9 | 🔥 **Passionate Creator** | Dedicated to creating and mastering their craft. |

---

## 🧩 Features
✨ Interactive **sliders** for lifestyle inputs  
🎯 Dynamic **persona visualization** (radar chart)  
🌙 Aesthetic **dark theme** interface  
🎉 **Emoji burst animation** for each persona  
💬 Personalized motivational quotes  
🚀 **Fast Streamlit deployment** with ML integration  

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (custom CSS + HTML)
- **Backend:** Python  
- **Machine Learning:** KMeans Clustering  
- **Visualization:** Matplotlib  
- **Libraries:** `numpy`, `pandas`, `matplotlib`, `joblib`, `scikit-learn`

---

📦 WellnessPersonas
│
├── app.py # Main Streamlit application
├── utils.py # Helper functions (ML logic, clustering rules)
├── model.pkl # Trained KMeans model
├── scaler.pkl # Data scaler
├── features.txt # Ordered list of input features
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## 🚀 Run Locally

If you want to run the app on your system:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/srijitabiswas/WellnessPersonas.git
cd WellnessPersonas

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
streamlit run app.py
Then open http://localhost:8501 in your browser.

💡 Authors

👩‍💻 Prakriti Sarkar
👩‍💻 Sresthita Nath
👩‍💻 Srijita Biswas

🪷 “Wellness is not a goal; it’s a way of living every day.”

🌍 Live Demo

👉 Explore the live app here:

🔗 https://wellnesspersonas-cthr6lsavffhyqmycxlyko.streamlit.app/
 

## 📂 Repository Structure
