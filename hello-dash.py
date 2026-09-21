import streamlit as st
import pandas as pd 
st.title("hey y mi scar😧")
dataframe = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(dataframe)
st.write("by danidani200")
