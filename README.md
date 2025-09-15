Wellness Personas of SNU 🎯

This project uses K-Means clustering on student lifestyle survey data to identify different wellness personas at SNU. The insights can help the Health Club design targeted wellness programs based on students’ habits and preferences.

📂 Project Structure
📁 Wellness-Personas-SNU
│── 📓 Untitled6.ipynb   # Jupyter Notebook with code
│── 📊 data.csv                  # Student survey dataset
│── 📄 README.md                 # Project documentation

⚙️ Methodology

Data Collection – Surveyed 111 students via Google Forms and exported as CSV.

Preprocessing – Cleaned missing values, removed outliers, standardized features.

Clustering – Applied K-Means, tested k=2–10, finalized k=4.

Evaluation – Used Silhouette score and Elbow method for validation.

Visualization – Heatmaps, scatterplots, and cluster distribution charts.

Insights – Created four student personas based on lifestyle traits.

🔍 Key Findings

Cluster 0 – Balanced Budgeters: Manage food + hobbies smartly.

Cluster 1 – Social Spenders: Spend more on outings, active in groups.

Cluster 2 – Low-Budget Hobbyists: Prioritize hobbies within a budget.

Cluster 3 – Minimalists: Spend less overall, limited participation.

📊 Results

The clustering revealed clear lifestyle groups.

Train Silhouette Score: 0.313

Test Silhouette Score: 0.121

Personas help design personalized wellness campaigns.

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/WellnessPersonas.git
cd WellnessPersonas


Install dependencies:

pip install -r requirements.txt


Open Jupyter Notebook:

jupyter notebook Untitled6.ipynb

📌 Future Scope

Add more lifestyle features (sleep, stress, exercise).

Explore other clustering methods (DBSCAN, Hierarchical).

Build a dashboard for interactive persona exploration.

👩‍💻 Contributors

Sresthita

Prakriti

Srijita
