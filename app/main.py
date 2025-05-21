import streamlit as st
from utils import load_data, get_ghi_summary
import pandas as pd
import matplotlib.pyplot as plt

st.title("Solar Farm Insights Dashboard")

# Country selection
countries = ["benin_clean", "sierrleon_clean", "togo_cleaned"]
selected_country = st.selectbox("Select Country", countries)

# Load data
df = load_data(selected_country)

# Display GHI boxplot
st.subheader("GHI Boxplot")
fig, ax = plt.subplots()
df["GHI"].plot(kind="box", ax=ax)
st.pyplot(fig)

# Show top regions table
st.subheader("GHI Summary")
summary = get_ghi_summary(df)
st.table(pd.DataFrame([summary], index=["Values"]))

# Interactive slider for GHI threshold
threshold = st.slider("Select GHI Threshold (W/m²)", min_value=0, max_value=1000, value=300)
st.write(f"Data points above {threshold} W/m²: {len(df[df['GHI'] > threshold])}")