# This is a Handwriting Analyzer Python script.
import base64
import time
import anthropic
import streamlit as st
from PIL import Image
from io import BytesIO
import os
from anthropic import Anthropic

anthropicSecretKey = "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"

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=anthropicSecretKey,

)
Client = Anthropic(
    api_key=os.environ.get("anthropicSecretKey"),
)
def  ask_claude(prompt,model="claude-3-opus-20240229"):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        temperature=0,
        system="You are a helpful AI assistant.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
user_input = "what is the capital of france?"
response = ask_claude(user_input)
print(f"Claude's response: {response}")
def analyze_handwriting(image_param):
    buffered = BytesIO()
    image_param.save(buffered, format="JPEG")
    image_data = base64.b64encode(buffered.getvalue()).decode()

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",

                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data
                        }
    },
                    {
                        "type": "text",
                        "text": """
                            Please analyze this handwriting or signature i want the result on french.
                            Describe the characteristics you observe and what they might indicate about the writer.
                            Include aspects like pressure, slant, size, spacing,
                            and any other notable features and result in json.
                        """

                    },
                ]
            }

        ]

    )

    return message.content[0].text

st.set_page_config(page_title="Analyser l'écriture manuscrite")
st.title("Analyser l'écriture manuscrite")
uploaded_file = st.file_uploader("Choisissez une image d'écriture manuscrite ou de signature.",
                                 type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Image téléchargée", use_column_width=True)
    # st.title("Analyser l'écriture manuscrite")

    if st.button("Analyser l'écriture manuscrite"):
        with st.spinner("Analyse en cours..."):

            analysis = analyze_handwriting(image)
            st.subheader("Résultats de l'analyse:")
            st.write(analysis)
