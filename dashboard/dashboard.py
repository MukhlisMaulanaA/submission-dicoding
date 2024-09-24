import streamlit as st
import pandas as pd
import json
import folium
from streamlit_folium import st_folium
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from folium import LinearColormap

# ----- DATA LOADING -----
# Load data sales per state
sales_per_state = pd.read_csv('dashboard/sales_per_state.csv')

# Load geojson data for Brazilian states
with open('./br_states.json') as f:
    geojson_data = json.load(f)

# Load data sales per category
sales_per_category = pd.read_csv('dashboard/category_sales.csv')

# ----- TRANSFORMATION -----
# Logarithmic transformation for price
sales_per_state['log_price'] = np.log(sales_per_state['price'] + 1)

# Create a dictionary to map seller_state to log_price
log_sales_dict = sales_per_state.set_index(
    'seller_state')['log_price'].to_dict()

with st.container():
  st.title("E-Commerce Sales Dashboard")
  
  # ----- TOP 10 SALES BY PRODUCT CATEGORY -----
  st.markdown("### Top 10 Kategori Produk Berdasarkan Penjualan")

  # Get top 10 categories by sales
  top_10_categories = sales_per_category.nlargest(10, 'price')

  # Create bar chart using Seaborn
  fig, ax = plt.subplots(figsize=(10, 6))
  sns.barplot(x='price', y='product_category_name_english',
              data=top_10_categories, palette='Blues_r', ax=ax)
  ax.set_title('Top 10 Kategori Produk berdasarkan Total Penjualan')
  ax.set_xlabel('Total Sales')
  ax.set_ylabel('Category')

  # Display the bar chart in Streamlit
  st.pyplot(fig)
  
  # ----- GEOSPATIAL VISUALIZATION -----
  st.markdown("### Distribusi Geografis Penjualan Berdasarkan Negara Bagian")

  # Set up Folium map
  # Center the map over Brazil
  m = folium.Map(location=[-15.7801, -47.9292], zoom_start=5)

  # Define colormap for sales data
  min_log_sales = min(log_sales_dict.values())
  max_log_sales = max(log_sales_dict.values())
  colormap = LinearColormap(
      colors=[(255, 246, 150), (6, 77, 0)], vmin=min_log_sales, vmax=max_log_sales)

  # Add GeoJson layer to the map
  for feature in geojson_data['features']:
      state_code = feature['properties']['SIGLA']
      log_total_sales = log_sales_dict.get(state_code, 0)

      folium.GeoJson(
          feature,
          style_function=lambda x, log_total_sales=log_total_sales: {
              # Use log-transformed sales to color the states
              'fillColor': colormap(log_total_sales),
              'color': 'black',
              'weight': 2,
              'fillOpacity': 0.7,
          },
          tooltip=f"State: {state_code}, Log Sales: {log_total_sales:.2f}"
      ).add_to(m)

  # Display the map
  st_folium(m, width=700, height=500)
  
# ----- INSIGHT SECTION -----
st.markdown("### Insight Utama")
st.markdown("""
- **Negara bagian SP** tetap mendominasi penjualan, bahkan setelah transformasi logaritmik diterapkan.
- **Kategori produk elektronik dan fashion** menduduki peringkat teratas dalam hal kontribusi terhadap total penjualan.
- Negara bagian seperti **RJ** dan **MG** memberikan kontribusi besar terhadap penjualan setelah SP, yang menunjukkan potensi peningkatan penjualan di masa depan.
""")
