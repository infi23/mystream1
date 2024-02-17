import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Membuat data acak
@st.cache_data
def get_data(n):
    data = pd.DataFrame({
        'x': range(n),
        'y': np.random.randn(n)
    })
    return data

# Slider untuk mengontrol jumlah data
n = st.sidebar.slider('Jumlah data', 10, 100, 50)
data = get_data(n)

# Menampilkan DataFrame
st.write(data)

# Membuat grafik
fig, ax = plt.subplots()
ax.scatter(data['x'], data['y'])

# Menambahkan slider untuk mengontrol batas y
y_max = st.sidebar.slider('Batas y atas', float(data['y'].min()), float(data['y'].max()), float(data['y'].max()))
ax.set_ylim([float(data['y'].min()), y_max])

# Menampilkan grafik
st.pyplot(fig)
