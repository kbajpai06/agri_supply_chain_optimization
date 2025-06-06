import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import openrouteservice
from openrouteservice import convert
import folium
from streamlit_folium import st_folium

# Load Data and Model
df = pd.read_csv("data/processed/inventory_dataset.csv")
model = joblib.load("models/inventory_predictor.pkl")

# Set Page Title
st.set_page_config(page_title="Agri Supply Chain Dashboard", layout="wide")
st.title("🌾 Intelligent Agricultural Supply Chain Optimization")

# Sidebar Filters
st.sidebar.header("📊 Filters")
crop = st.sidebar.selectbox("Select Crop", sorted(df["Crop"].unique()))
state = st.sidebar.selectbox("Select State", sorted(df["State"].unique()))
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))

# Filtered Data
filtered_df = df[(df["Crop"] == crop) & (df["State"] == state) & (df["Year"] == year)]
sample = filtered_df.iloc[0:1]

# Prepare for Prediction
sample_encoded = pd.get_dummies(sample.drop(columns=["Inventory_Required"]))
model_columns = model.feature_names_in_
for col in model_columns:
    if col not in sample_encoded.columns:
        sample_encoded[col] = 0
sample_encoded = sample_encoded[model_columns]
predicted = model.predict(sample_encoded)[0]

# Inventory Risk Level
if predicted > 3000:
    risk_level = "🔴 High Risk (Overstock)"
elif predicted < 500:
    risk_level = "🟡 Low Risk (Understock)"
else:
    risk_level = "🟢 Optimal"

# Display Prediction
st.subheader(f"📦 Predicted Inventory for {crop} in {state} ({year}):")
st.metric(label="Inventory Requirement (tons)", value=f"{predicted:.2f}", delta=None)
st.info(f"Risk Level: {risk_level}")

# Forecasted Demand Trend
st.subheader("📈 Forecasted Demand (Avg Inventory Per Year)")
demand_trend = df[(df["Crop"] == crop) & (df["State"] == state)].groupby("Year")["Inventory_Required"].mean().reset_index()
fig = px.line(demand_trend, x="Year", y="Inventory_Required", title=f"Inventory Demand Forecast for {crop} in {state}")
st.plotly_chart(fig, use_container_width=True)

# Route Optimization (Simulated example with dummy coordinates)
st.subheader("🛣️ Optimized Transport Route Map")
try:
    client = openrouteservice.Client(key="5b3ce3597851110001cf6248c499806c1caa4c3f9b1a288cc319b000")  # Replace with your ORS API Key
    coords = ((76.7794, 30.7333), (76.9558, 30.2110))  # Dummy coordinates
    route = client.directions(coords)
    geometry = convert.decode_polyline(route['routes'][0]['geometry'])

    # Build Map
    m = folium.Map(location=[30.5, 76.8], zoom_start=9)
    folium.Marker(location=[30.7333, 76.7794], popup="Warehouse").add_to(m)
    folium.Marker(location=[30.2110, 76.9558], popup="Farm").add_to(m)
    folium.PolyLine(locations=[(lat, lon) for lon, lat in geometry['coordinates']], color="blue").add_to(m)

    st_data = st_folium(m, width=700)
except:
    st.warning("Could not load route map. Ensure OpenRouteService API key is valid.")

# Full Data Preview
with st.expander("🔍 View Full Filtered Data"):
    st.dataframe(filtered_df)

st.markdown("---")
st.caption("Built for smart agriculture and efficient supply chain management 🚜")



