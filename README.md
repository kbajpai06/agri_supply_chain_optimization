🌾Intelligent Agricultural Supply Chain Optimization
This project aims to modernize and optimize the agricultural supply chain in India by forecasting crop demand, predicting inventory needs, and mapping efficient transport routes. It leverages machine learning, time series forecasting, and real-time mapping APIs to assist in strategic decision-making for farmers, suppliers, and logistics managers.

🚀 Features
📦 Inventory Forecasting: Predicts inventory requirements for various crops using historical and synthetic data.
📈 Demand Trend Visualization: Displays year-wise trends in average inventory requirements to assess crop demand.
🛣️ Route Optimization: Visualizes the most efficient route from farms to warehouses to retailers using OpenRouteService API.
🔍 Interactive Dashboard: Built with Streamlit to allow users to filter by year, crop, and state for dynamic insights.
⚠️ Inventory Risk Analysis: Automatically detects overstocking or understocking risk based on predicted inventory.

🧠Tech Stack
-Python, Pandas, scikit-learn, Prophet
-Streamlit (dashboard)
-Plotly (visualizations)
-OpenRouteService API (route mapping)
-Folium (interactive maps)
-Joblib (model serialization)

▶️How to Run
1.Install dependencies:
-- pip install -r requirements.txt

2.Launch the dashboard:
-- streamlit run dashboard.py

📌 Notes
-Forecasts are generated using the Prophet model and extended using synthetic data for future predictions.

-Inventory prediction uses a Random Forest Regressor trained on crop, state, year, and storage parameters.

-Real-time route optimization is done using dummy coordinates; replace them for your real use case.


🙌 Author
Developed by Kartik Bajpai — for academic and practical applications in agri-tech and supply chain analytics.


