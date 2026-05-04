# 🏀 Army Basketball Visualization

This project is a Streamlit web application that allows users to compare Army basketball players with professional players using interactive radar charts. The goal is to explore statistical similarities and differences between players in a clean, visual way.

---

## 📊 Features

- Select an Army basketball player
- Automatically filter professional players by class
- Choose which statistics to visualize
- Generate interactive radar charts using Plotly
- Simple and intuitive interface powered by Streamlit
- view team stats for top 5 players on offense, defense and shooting
---

## 🛠️ Technologies Used

- Python
- pandas
- plotly
- streamlit

---

## 📦 Requirements

Install all dependencies with:

```bash
pip install pandas plotly streamlit
```

Or use a `requirements.txt` file:

```
pandas
plotly
streamlit
```

---

## ▶️ How to Run the App

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

2. Run the Streamlit app:

```bash
streamlit run v2.py
```

3. Open the local URL provided in your terminal (usually http://localhost:8501)

---

## 📁 Project Structure

```
.
├── Player.py
├── Army_mens_basketball.csv
├── Pro_Players_College.csv
├── requirements.txt
├── Teams.py
├── streamlit_app.py
├── patriot_league_per_game.csv
└── README.md
```

---

## 📈 How It Works

- Loads player data using pandas
- Filters players based on selected criteria (e.g., class)
- Allows user-selected statistics for comparison
- Uses Plotly to generate radar charts for visualization
- Displays everything in a Streamlit web interface

---

## ⚠️ Notes

- This project is still under development
- Features and functionality may change
- Some statistics may need normalization for more accurate comparisons
- Future improvements may include:
  - Separation of percentage vs counting stats

---

## 📬 Author

Gael Gama  
United States Military Academy (West Point)
