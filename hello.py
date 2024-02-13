import streamlit as st

st.write(
    """
    # Contoh streamlit
    Halo saya wisnu

    """
)
#########################
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)
######################
import pandas as pd
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))
##################
st.title('Belajar Analisis Data')
##################
st.header('Pengembangan Dashboard')
#######################
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

#####################
import matplotlib.pyplot as plt
import numpy as np
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

####################
name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)
###################
text = st.text_area('Feedback')
st.write('Feedback: ', text)
################
number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')
####################
import datetime
date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)
#################
uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
#################
if st.button('Say hello'):
    st.write('Hello there')    
####################
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')

######################
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)
###########################
genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
############
genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)
##############
values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0, 100))
st.write('Values:', values)
