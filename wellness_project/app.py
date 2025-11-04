# app.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import streamlit.components.v1 as components
from utils import (
    load_model_and_scaler,
    load_feature_order,
    preprocess_user_input,
    rule_based_cluster,
    get_cluster_description
)

# 🌙 PAGE SETUP
st.set_page_config(page_title="Wellness Personas of SNU", page_icon="💪", layout="wide")

# 💫 DARK THEME & STYLE
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(-45deg, #0a0f1c, #121826, #1a1f2e, #101522);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            color: #f5f5f5;
        }
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #181a20 0%, #1f2229 100%) !important;
            color: #fafafa;
            border-right: 1px solid #00bcd440;
            box-shadow: 0 0 15px #00bcd422;
        }
        .persona-card {
            background-color: #1c1e26;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(0, 188, 212, 0.15);
            border: 1px solid #00bcd455;
            transition: all 0.3s ease-in-out;
        }
        .persona-card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 50px rgba(0, 188, 212, 0.4);
            border-color: #00eaff;
        }
        .stButton button {
            background: linear-gradient(90deg, #00bcd4, #4dd0e1);
            color: white;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 0 0 15px #00bcd455;
        }
        .stButton button:hover {
            background: linear-gradient(90deg, #4dd0e1, #00bcd4);
            box-shadow: 0 0 25px #00bcd4;
            transform: scale(1.05);
        }
        .footer {
            text-align: center;
            color: #888;
            font-size: 14px;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
    <div style='text-align:center; padding:20px 0;'>
        <h1 style='font-size:45px; color:#00e0ff;'>💪 Wellness Personas of SNU</h1>
        <p style='font-size:18px; color:#ddd;'>Uncover your lifestyle cluster and discover what makes you unique 🌿</p>
    </div>
""", unsafe_allow_html=True)

# LOAD MODEL
model, scaler = load_model_and_scaler()
features = load_feature_order()

# SIDEBAR
st.sidebar.markdown("## ✨ Enter Your Lifestyle Details")
st.sidebar.markdown("Rate yourself from 0️⃣ (least) to 🔟 (most) on each parameter below.")
st.sidebar.markdown("---")

user_input = {}
for feature in features:
    user_input[feature] = st.sidebar.slider(
        label=f"🔹 {feature.replace('_', ' ').capitalize()}",
        min_value=0,
        max_value=10,
        value=5,
        help=f"Rate your {feature.replace('_', ' ')} from 0 to 10"
    )

# ACTION
if st.sidebar.button("🌟 Reveal My Persona"):
    processed, used_features = preprocess_user_input(user_input, features, scaler)
    cluster = rule_based_cluster(user_input)
    description = get_cluster_description(cluster)

    persona_emojis = ["💪", "🍰", "🎨", "🧘‍♀️", "🎧", "⚡", "🌈", "🔥", "📚", "🌿"]
    emoji = persona_emojis[cluster % len(persona_emojis)]

    colors = ["#ff9f1c", "#2ec4b6", "#e71d36", "#ff7f50", "#6a4c93",
              "#3a86ff", "#8338ec", "#ff006e", "#00ff88", "#f4a261"]
    color = colors[cluster % len(colors)]

    left, right = st.columns([1, 1])
    with left:
        st.markdown(
            f"""
            <div class="persona-card" style="border-left: 10px solid {color};">
                <h2 style="color:{color}; font-size:34px;">{emoji} Persona {cluster}</h2>
                <p style="font-size:22px; font-weight:600; color:#f5f5f5;">{description}</p>
                <p style="color:#bbb; font-size:16px;">
                    💡 Your choices reflect your personality in unique ways. Keep exploring balance and wellness!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        labels = list(user_input.keys())
        stats = list(user_input.values())
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
        stats += stats[:1]
        angles += angles[:1]
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
        ax.fill(angles, stats, color=color, alpha=0.4)
        ax.plot(angles, stats, color=color, linewidth=2)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, color="#ccc", size=11)
        ax.set_title("✨ Your Lifestyle Radar", color=color, size=14, pad=20)
        fig.patch.set_facecolor("#1c1e26")
        ax.set_facecolor("#1c1e26")
        st.pyplot(fig)

    # 🎉 EMOJI BURST (NOW FULLY WORKING)
    components.html(
        f"""
        <html>
        <head>
            <style>
                body {{
                    margin: 0;
                    background: transparent;
                    overflow: hidden;
                }}
                .emoji {{
                    position: absolute;
                    font-size: 2rem;
                    opacity: 0;
                    animation: fly 2s ease-out forwards;
                }}
                @keyframes fly {{
                    0% {{
                        transform: translate(0, 0) scale(1);
                        opacity: 1;
                    }}
                    100% {{
                        transform: translate(var(--x), var(--y)) scale(0.5);
                        opacity: 0;
                    }}
                }}
            </style>
        </head>
        <body>
            <div id="emoji-container"></div>
            <script>
                const container = document.getElementById("emoji-container");
                const emojis = "{emoji}".repeat(25).split("");
                emojis.forEach(e => {{
                    const span = document.createElement("span");
                    span.classList.add("emoji");
                    span.textContent = e;
                    span.style.left = Math.random() * 100 + "vw";
                    span.style.top = "80vh";
                    const dx = (Math.random() * 200 - 100);
                    const dy = - (Math.random() * 400 + 100);
                    span.style.setProperty("--x", dx + "px");
                    span.style.setProperty("--y", dy + "px");
                    span.style.animationDelay = (Math.random() * 0.5) + "s";
                    container.appendChild(span);
                    setTimeout(() => span.remove(), 2500);
                }});
            </script>
        </body>
        </html>
        """,
        height=300,
    )

    st.markdown("<h3 style='color:#00bcd4;'>🧩 Your Lifestyle Scores</h3>", unsafe_allow_html=True)
    st.json(user_input)

    st.markdown(
        f"""
        <div style='text-align:center; background-color:{color}15;
                    padding:20px; border-radius:15px; margin-top:30px;'>
            <h4 style='color:{color}; font-size:20px;'>
                🌼 “Wellness is not a goal; it's a way of living every day.” {emoji}
            </h4>
        </div>
        """, unsafe_allow_html=True
    )

else:
    st.markdown("""
        <div style='text-align:center; margin-top:60px;'>
            <img src="https://cdn-icons-png.flaticon.com/512/2645/2645897.png" width="150">
            <h3 style='color:#eee;'>👈 Use the sidebar sliders to find your wellness persona!</h3>
            <p style='color:#ccc;'>Understand your habits, celebrate your style, and explore your path to balance 💖</p>
        </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <div class='footer'>
        <hr style='border-color:#333;'>
        Made by <b style='color:#00bcd4;'>Prakriti</b>, <b style='color:#00bcd4;'>Sresthita</b>, and <b style='color:#00bcd4;'>Srijita</b> <br>
        <span style='font-size:13px; color:#888;'>Wellness Personas of SNU © 2025</span>
    </div>
""", unsafe_allow_html=True)
