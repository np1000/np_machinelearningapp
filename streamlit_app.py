import streamlit as st
import pandas as pd
st.title('🎈 Machine learning App')

st.info('This app builds a machine learning model')
with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

st.write('**X**')
X=df.drop('species',axis=1)
X

st.write('**Y**')
y = df.species
y
#species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex#
with st.expander('Data Visulaisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y= 'body_mass_g' color ='species')
