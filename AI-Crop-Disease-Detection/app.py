import streamlit as st
from PIL import Image
import io
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def detect_disease_with_gemini(image_bytes):
    """
    Detect crop disease using Gemini and recommend mitigation strategies based on the uploaded image.
    """
    try:
        img = Image.open(io.BytesIO(image_bytes))
        img.save("temp_crop_image.jpg")

        # Upload the image file (assuming 'media' is a valid path, here using the temporary file)
        myfile = genai.upload_file("temp_crop_image.jpg")

        # Print the uploaded file details (for debugging purposes)
        print(f"Uploaded file: {myfile}")

        # Create a generative model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate content based on the image and a relevant prompt (crop disease analysis)
        prompt_text = "\n\nCan you analyze the diseases visible in this crop image and suggest mitigation strategies?"
        result = model.generate_content([myfile, prompt_text])

        # Process the result
        analysis = result.text if result else "No analysis or invalid response."

    except Exception as e:
        raise RuntimeError(f"Error processing the image: {e}")

    return analysis


# Streamlit UI setup
st.title("Crop Disease Detection")
st.markdown(
    "Upload a crop image to detect potential diseases and get recommendations for mitigation."
)

# File uploader
uploaded_file = st.file_uploader("Upload a Crop Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert the image to bytes for processing
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes = img_bytes.getvalue()

        # Process the image using Gemini
        st.write("Processing the image using Gemini...")
        analysis = detect_disease_with_gemini(img_bytes)

        # Display the result
        st.write("**Analysis Result:**", analysis)

    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.info("Please upload an image to begin detection.")
