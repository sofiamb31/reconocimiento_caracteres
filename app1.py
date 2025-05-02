import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Reconocimiento óptico de Caracteres")
image = Image.open('ocr imagen.jpeg')

st.image(image,width=300)
image = Image.open('ayuda.jpg')

st.image(image,width=300)
img_file_buffer = st.camera_input("Toma una Foto que contenga letras y esta página lo convertira en un texto")

with st.sidebar:
      filtro = st.radio("Aplicar Filtro",('Con Filtro', 'Sin Filtro'))


if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    if filtro == 'Con Filtro':
         cv2_img=cv2.bitwise_not(cv2_img)
    else:
         cv2_img= cv2_img
    
        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 
    

st.markdown("""
    <style>
        body {
            background-color: #f0f0f0; /
        }
        .stApp {
            background-color: #ADD8E6; /
        }
    </style>
    """, unsafe_allow_html=True)
    


