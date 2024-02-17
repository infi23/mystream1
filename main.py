import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.write("Infinity Coding Club")
# Membuat data dari dictionary
data = {
    'id': [1, 2, 3, 4, 5],
    'nama': ['Ali', 'Budi', 'Charlie', 'Dani', 'Eko'],
    'usia': [30, 25, 35, 40, 45],
    'pekerjaan': ['Dokter', 'Insinyur', 'Guru', 'Petani', 'Pengusaha']
}
#data = pd.read_csv('data.csv')

df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write(df)

# Membuat grafik batang dari kolom 'nama' dan 'usia'
fig, ax = plt.subplots()
ax.bar(df['nama'], df['usia'])
plt.title('Usia berdasarkan Nama')
plt.xlabel('Nama')
plt.ylabel('Usia')

# Menampilkan grafik
st.pyplot(fig)
