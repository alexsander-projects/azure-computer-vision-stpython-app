import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Azure Computer Vision API endpoint and subscription key
vision_base_url = "<YOUR_vision_base_url>"
ocr_url = vision_base_url + "vision/v3.0/ocr"
subscription_key = "<YOUR_subscription_key>"

headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}


def get_prediction(input_image):
    # Convert image to bytes
    image_bytes = BytesIO()

    # Convert image to RGB mode if it's in RGBA mode
    if input_image.mode == 'RGBA':
        input_image = input_image.convert('RGB')

    input_image.save(image_bytes, format='JPEG')
    image_bytes = image_bytes.getvalue()

    response = requests.post(
        ocr_url, headers=headers, data=image_bytes)
    response.raise_for_status()

    analysis = response.json()
    text = ' '.join([word['text'] for region in analysis['regions'] for line in region['lines'] for word in line['words']])
    return text


@st.cache
def cached_prediction(input_image):
    return get_prediction(input_image)


def main():
    st.title("OCR prediction")
    st.write("This application can read text from an image.")

    image_file = st.file_uploader("Upload an image")

    if image_file:
        input_image = Image.open(image_file)
        # Display the uploaded image
        st.image(input_image, caption="Uploaded image", use_column_width=True)
        pred_button = st.button("Analyze")

        if pred_button:
            prediction = cached_prediction(input_image)
            st.title("Analysis result:")
            st.write(prediction)


if __name__ == '__main__':
    main()
