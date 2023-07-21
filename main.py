import streamlit as st 
import numpy as np 
import pandas as pd
from PIL import Image

st.title("streamlit 超入門")

st.write("Display Image")

img = Image.open("sample.png")
st.image(img, caption="Suzuki", use_column_width=True)