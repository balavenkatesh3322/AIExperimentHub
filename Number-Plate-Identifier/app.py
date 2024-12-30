import streamlit as st
from PIL import Image
import io
import os
import google.generativeai as genai

# Configure the AI API with the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def detect_vehicle_details_and_violations(image_bytes):
    """
    Extract number plate number, vehicle model details, and detect violations such as helmet absence.
    """
    temp_image_path = "temp_vehicle_image.jpg"
    try:
        # Save the image temporarily
        img = Image.open(io.BytesIO(image_bytes))
        img.save(temp_image_path)

        # Upload the image to the AI system
        myfile = genai.upload_file(temp_image_path)

        # Debug: Print uploaded file details
        print(f"Uploaded file: {myfile}")

        # Create a generative model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Updated prompt to include violation detection
        prompt_text = (
            "This is an image of a vehicle. Please extract the following details:\n\n"
            "- Number plate number\n"
            "- Vehicle type (e.g., car, bike, truck, etc.)\n"
            "- Vehicle model or brand details\n"
            "- Any safety violations visible (e.g., no helmet, overcrowding, etc.)\n\n"
            "Present the extracted details clearly and concisely."
        )

        # Generate response
        result = model.generate_content([myfile, prompt_text])

        # Extract text from the response
        details = result.text if result else "No details detected or invalid response."

    except Exception as e:
        raise RuntimeError(f"Error processing the image: {e}")

    finally:
        # Cleanup: Delete the temporary image file
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)

    return details


# Streamlit UI setup
st.title("Vehicle Details and Violation Detection")
st.markdown(
    "Upload an image of a car, bike, or any vehicle to extract details like number plate, model, and detect any safety violations."
)

# File uploader
uploaded_file = st.file_uploader("Upload a Vehicle Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert the image to bytes for processing
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes = img_bytes.getvalue()

        # Add spinner while processing
        with st.spinner("Processing the image... Please wait."):
            details = detect_vehicle_details_and_violations(img_bytes)

        # Beautify and display the result
        st.markdown("### **Extracted Vehicle Information and Violations:**")
        st.success(details)  # Use success box for a clean display

    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.info("Please upload an image to begin extraction.")
