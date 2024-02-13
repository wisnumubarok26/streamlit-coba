import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_day = pd.read_csv("day.csv", index_col='instant')
data1 = data_day[['season','casual','registered','cnt']]
data_day['yr'] = data_day['yr'].replace({0: 2011, 1: 2012})

penjualan_permusim = data1.groupby('season')['cnt'].sum()
total_penjualan = data_day.groupby('yr')['cnt'].sum()

def show_bar_plot(total_penjualan):
    # Membuat plot
    fig, ax = plt.subplots(figsize=(8, 6))
    total_penjualan.plot(kind='bar', color=['blue', 'orange'], ax=ax)
    ax.set_title('Perbandingan Peminjaman Tahun 2011 dan 2012')
    ax.set_xlabel('yr')
    ax.set_ylabel('Total Peminjaman')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.grid(axis='y')

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

def show_bar_plot2(penjualan_permusim):
    # Membuat plot
    fig, ax = plt.subplots(figsize=(12, 6))
    penjualan_permusim.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Peminjaman sepeda per Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Total Peminjaman')
    ax.set_xticks(range(0, 4),['Springer', 'Summer', 'Fall', 'Winter'], rotation=45)
    # ax.set_xticklabels()
    ax.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)

st.title('Dasboard Analisa Peminjaman Sepeda 2011-2012')
# with st.sidebar:
    
#     st.text('Muhamad Wisnu Mubarok')
#     st.text('wisnumubarok2002@gmail.com')
# st.title('Belajar Analisis Data')
st.write(data_day)
 

st.title("Peminjaman pertahun")
show_bar_plot(total_penjualan)
 

st.title("Penjualan permusim")
show_bar_plot2(penjualan_permusim)    

st.text('Muhamd Wisnu Mubarok')