 🌾 Agricultural Supply Chain Optimization

An intelligent, data-driven system for forecasting crop production, predicting inventory requirements, and optimizing transport routes across Indian states. This project leverages Machine Learning and Time Series Forecasting to modernize and streamline the agricultural supply chain for better efficiency, reduced wastage, and smarter planning.

📌 Features

- 📊 **Production Forecasting**: Uses Prophet to forecast crop production for future years based on historical data (1997–2025).
- 📦 **Inventory Prediction**: Machine Learning (Random Forest Regressor) predicts inventory requirements using synthetic inventory datasets.
- 🗺️ **Route Optimization**: Visualizes optimized transportation routes using OpenRouteService API.
- 📈 **Interactive Dashboard**: Built with Streamlit and Plotly for real-time exploration of crop-wise and state-wise inventory needs and trends.
- ☁️ **Real-Time Weather & Future Planning**: Extendable for weather integration and real-time insights for policy makers, farmers, and distributors.

🚀 Getting Started
 1. Clone the Repository
```bash
git clone https://github.com/your-username/agri_supply_chain_optimization.git
cd agri_supply_chain_optimization
```

2. Install Dependencies
-Create a virtual environment (optional but recommended):
```python -m venv venv```
```source venv/bin/activate  # On Windows: venv\Scripts\activate```
-Install required libraries:
```pip install -r requirements.txt```

3. Start the Dashboard
```streamlit run dashboard.py```

📉 Inventory Forecasting
The inventory prediction is performed using a Random Forest Regressor model trained on a synthetic but realistic dataset that includes:
-Crop type
-State
-Year
-Forecasted demand
-Last year’s inventory
-Storage capacity

📈 These forecasts are visualized on the dashboard by year, helping predict understock/overstock scenarios.

🔮 Crop Production Forecasting
-Utilizes Facebook Prophet to forecast future crop production:
-Trained on region-wise crop production dataset (1997–2025)
-Predicts up to year 2028
-Model supports all crops and states in a loop
-Output can be integrated into inventory or supply chain planning

🛣️ Route Optimization
-Although simplified in this version, it includes:
-Simulated coordinates (e.g., Chandigarh to Patiala)
-Real route plotted using OpenRouteService API
-Extendable for dynamic routes using warehouse/farm GPS data

🧠 Technologies Used
-Python
-Pandas, NumPy
-Prophet, scikit-learn
-Streamlit, Plotly, Folium
-OpenRouteService API

📌 Example Use Cases
📍 State agriculture departments planning seed or fertilizer dispatches
📍 Distributors tracking overstock/understock risks
📍 NGOs targeting support to areas with underproduction risk
📍 Retailers managing demand in advance for high-yield crops

🙌 Acknowledgements
-Kaggle - Crop Production Statistics Dataset
-Facebook Prophet
-OpenRouteService API

🧑‍💻 Author
Kartik Bajpai 
Software Engineering Student @ DTU
💻 MERN Stack • ML Enthusiast • Backend & Data Science








