import streamlit as st
from PIL import Image
import io
import os
import google.generativeai as genai
import tempfile

# Initialize Gemini API key (make sure to set your environment variable)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_threats_and_mitigations(image_bytes, file_extension):
    """
    Analyze the uploaded threat modeling diagram and provide suggested threats and mitigation strategies.
    """
    try:
        # Create a unique temporary file using tempfile with the same extension as the original image
        temp_filename = tempfile.mktemp(
            suffix=file_extension
        )  # Generate a unique temp file name with original extension

        # Save the image to the temporary file
        img = Image.open(io.BytesIO(image_bytes))
        img.save(temp_filename)

        # Upload the image file (temporary file)
        myfile = genai.upload_file(temp_filename)

        # Print the uploaded file details (for debugging purposes)
        print(f"Uploaded file: {myfile}")

        # Create a generative model instance
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Prompt text to analyze the threat modeling image
        prompt_text = "\n\nCan you analyze the threats and security issues visible in this threat model diagram and suggest mitigation strategies?"

        # Generate content based on the image and the prompt
        result = model.generate_content([myfile, prompt_text])

        # Process the result
        analysis = result.text if result else "No analysis or invalid response."

    except Exception as e:
        raise RuntimeError(f"Error processing the image: {e}")

    finally:
        # Delete the temporary file after use
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

    return analysis


# Streamlit UI setup
st.title("Threat Modeling Analysis")
st.markdown(
    "Upload a architecture image to analyze potential threats and receive mitigation strategies."
)

# File uploader
uploaded_file = st.file_uploader(
    "Upload a application architecture Diagram", type=["jpg", "jpeg", "png", "svg"]
)

if uploaded_file is not None:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(
            image, caption="Uploaded Threat Modeling Diagram", use_container_width=True
        )

        # Get the file extension to match the uploaded image format
        file_extension = os.path.splitext(uploaded_file.name)[
            1
        ].lower()  # Extract file extension (e.g., .jpg, .png)

        # Convert the image to bytes for processing
        img_bytes = io.BytesIO()
        image.save(img_bytes, format=image.format)
        img_bytes = img_bytes.getvalue()

        # Display the spinner while processing the image
        with st.spinner("Processing the diagram for threat analysis..."):
            # Process the image using Gemini
            analysis = analyze_threats_and_mitigations(img_bytes, file_extension)

        # Display the result
        st.write("**Analysis Result:**", analysis)

        # Provide relevant links and references for further reading
        st.markdown("### Recommended Resources for Mitigations:")
        st.markdown(
            "- **OWASP Top 10**: [OWASP Top 10 Project](https://owasp.org/www-project-top-ten/)"
        )
        st.markdown(
            "- **STRIDE Threat Model**: [STRIDE Overview](https://learn.microsoft.com/en-us/security/engineering/stride-methodology)"
        )
        st.markdown(
            "- **NIST Cybersecurity Framework**: [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)"
        )

    except Exception as e:
        st.error(f"Error processing the image: {e}")
else:
    st.info("Please upload an image to begin threat modeling analysis.")
