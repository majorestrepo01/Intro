import streamlit as st
from PIL import Image

st.title("la primera app de Maria José en Streamlit")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backbend y frontend.")
image = Image.open('Pinkaura.JPG')
st.image(image, caption='Interfaces multimodales')

