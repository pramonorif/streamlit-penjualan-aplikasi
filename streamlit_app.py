import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Dashboard Penjualan Sederhana",
    layout="wide"
)

# 2. Judul dan Deskripsi
st.title("💰 Dashboard Analisis Penjualan Bulanan")
st.markdown("Aplikasi sederhana yang dibuat dengan Python dan Streamlit.")
st.divider() # Garis pemisah

# 3. Data
data = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Penjualan': [15000, 18000, 22000, 19000, 25000, 28000],
    'Biaya_Iklan': [2000, 2500, 3000, 2200, 3500, 3800]
}
df = pd.DataFrame(data)

# 4. Tampilkan Statistik Utama (Key Performance Indicators/KPI)
total_penjualan = df['Penjualan'].sum()
rata_rata_iklan = df['Biaya_Iklan'].mean()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Penjualan", f"Rp {total_penjualan:,.0f}")
with col2:
    st.metric("Rata-rata Biaya Iklan", f"Rp {rata_rata_iklan:,.0f}")

st.divider()

# 5. Tampilkan Grafik
st.header("Visualisasi Data Penjualan")

# Membuat grafik batang (Matplotlib)
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df['Bulan'], df['Penjualan'], color='teal')
ax.set_title('Penjualan per Bulan')
ax.set_xlabel('Bulan')
ax.set_ylabel('Penjualan (IDR)')
ax.grid(axis='y', linestyle='--')

# Menampilkan figure Matplotlib di Streamlit
st.pyplot(fig)

# 6. Tampilkan Data Mentah
st.subheader("Data Mentah")
st.dataframe(df)
