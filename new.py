import streamlit as st
import pandas as pd
from io import BytesIO
from PIL import Image
import base64

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the uploaded file as bytes
    bytes_data = uploaded_file.getvalue()

    # Decode the bytes data using base64
    decoded_data = base64.b64decode(bytes_data)

    # Create a BytesIO object from the decoded data
    bytes_io = BytesIO(decoded_data)

    # Open the image file
    image = Image.open(bytes_io)
    st.image(image, caption="image", use_column_width=True)

    # Encode and decode a sample string using base64
    data = b'Python bytes to base64'
    encoded_data = base64.b64encode(data)
    print(encoded_data.decode())

    # Read the file as a CSV file
    dataframe = pd.read_csv(BytesIO(decoded_data))
    st.write(dataframe)