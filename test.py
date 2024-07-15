import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image
import base64

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Read the uploaded file as bytes
    bytes_data = uploaded_file.getvalue()

    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="image", use_column_width=True)

    # Convert the image to base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_data = base64.b64encode(buffered.getvalue()).decode()

    st.write("Base64 encoded image:")
    st.write(image_data)

    # Read the CSV file using pandas
    dataframe = pd.read_csv(uploaded_file)
    st.write("CSV Dataframe:")
    st.write(dataframe)