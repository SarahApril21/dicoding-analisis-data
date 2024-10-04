# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set the seaborn style for plots
sns.set(style='dark')

# Load datasets
day_data = pd.read_csv('D:\MBKM\BANGKIT 2024\PROJECTS\#1 DICODING\Belajar Analisis Data dengan Python_Sarah Aprilia Hasibuan\perbaikan\data\day.csv')  
hour_data = pd.read_csv('D:\MBKM\BANGKIT 2024\PROJECTS\#1 DICODING\Belajar Analisis Data dengan Python_Sarah Aprilia Hasibuan\perbaikan\data\hour.csv')

# Convert 'dteday' to datetime in both datasets
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

# Merge the day and hour datasets based on 'dteday'
merged_data = pd.merge(day_data, hour_data, on='dteday', how='outer', suffixes=('_day', '_hour'))

# Save the combined dataset to a CSV file
merged_data.to_csv('combination_data.csv', index=False)

# Streamlit setup for sidebar and date filtering
st.header("Bike Sharing Data Dashboard :sparkles:")
with st.sidebar:

    st.image("https://www.shutterstock.com/image-vector/mountain-biking-cycling-logo-abstract-600nw-2170224863.jpg")

# Set date filters
min_date = merged_data['dteday'].min()
max_date = merged_data['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    "Date Range", [min_date, max_date],
    min_value=min_date, max_value=max_date
)

filtered_data = merged_data[(merged_data['dteday'] >= min_date) & (merged_data['dteday'] <= max_date)]

st.subheader('Jumlah Penyewaan Berdasarkan Faktor Cuaca dan Hari dalam Seminggu')

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='weekday_day', y='cnt_hour', hue='weathersit_day', data=filtered_data, palette='coolwarm', ax=ax)
ax.set_title('Jumlah Penyewaan Berdasarkan Cuaca dan Hari dalam Seminggu', fontsize=20)
ax.set_xlabel('Hari dalam Seminggu (0 = Minggu, 6 = Sabtu)', fontsize=15)
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=15)
ax.legend(title='Kondisi Cuaca (1 = Cerah, 2 = Mendung, 3 = Hujan)', title_fontsize=12, fontsize=10)
st.pyplot(fig)

st.subheader("Rata-rata Penyewaan Pengguna Kasual Berdasarkan Hari Kerja dan Cuaca")
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x="weathersit_day", y="casual_hour", hue="workingday_day", data=filtered_data, palette="coolwarm", ax=ax)
ax.set_title("Rata-rata Penyewaan Pengguna Kasual Berdasarkan Hari Kerja dan Cuaca", fontsize=20)
ax.set_xlabel("Kondisi Cuaca", fontsize=15)
ax.set_ylabel("Rata-rata Pengguna Kasual", fontsize=15)
ax.legend(title="Hari Kerja", title_fontsize=12, fontsize=10)
st.pyplot(fig)

st.subheader("Rata-rata Penyewaan Pengguna Terdaftar Berdasarkan Hari Kerja dan Cuaca")
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x="weathersit_day", y="registered_hour", hue="workingday_day", data=filtered_data, palette="coolwarm", ax=ax)
ax.set_title("Rata-rata Penyewaan Pengguna Terdaftar Berdasarkan Hari Kerja dan Cuaca", fontsize=20)
ax.set_xlabel("Kondisi Cuaca", fontsize=15)
ax.set_ylabel("Rata-rata Pengguna Terdaftar", fontsize=15)
ax.legend(title="Hari Kerja", title_fontsize=12, fontsize=10)
st.pyplot(fig)

st.subheader("Rata-rata Total Penyewaan Sepeda Berdasarkan Hari Kerja dan Cuaca")
fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x="weathersit_day", y="cnt_hour", hue="workingday_day", data=filtered_data, palette="coolwarm", ax=ax)
ax.set_title("Rata-rata Total Penyewaan Sepeda Berdasarkan Hari Kerja dan Cuaca", fontsize=20)
ax.set_xlabel("Kondisi Cuaca", fontsize=15)
ax.set_ylabel("Rata-rata Total Penyewaan", fontsize=15)
ax.legend(title="Hari Kerja", title_fontsize=12, fontsize=10)
st.pyplot(fig)

st.caption("Copyright © Dicoding 2024")