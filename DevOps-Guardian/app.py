import streamlit as st
import google.generativeai as genai
import os


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("Please set your Google Gemini API key.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)


# Function to analyze configuration files with Google Gemini
def analyze_with_gemini(file_content):
    """
    Analyze the given DevOps configuration file for misconfigurations
    and provide remediation suggestions using Google Gemini.
    """
    try:
        prompt = f"""
        You are an AI DevOps assistant. Analyze the following configuration file for misconfigurations, 
        vulnerabilities, and best practice violations. Provide a detailed report of issues and actionable remediation steps.

        Configuration File:
        {file_content}
        """
        model = genai.GenerativeModel("gemini-1.5-flash")
        result = model.generate_content([prompt])
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"


# Streamlit App
st.title("🔒 AI-DevOps Guardian")
st.subheader("Secure your DevOps configurations with AI-powered analysis.")
st.write(
    """
Upload your DevOps configuration files (e.g., YAML, JSON, Dockerfile, Terraform, Ansible, Kubernetes) to scan for:
- Misconfigurations
- Security vulnerabilities
- Best practice violations
- Actionable remediation suggestions
"""
)

# File Upload Section
uploaded_file = st.file_uploader(
    "Upload a DevOps configuration file",
    type=["yaml", "yml", "json", "tf", "ini", "conf", "Dockerfile"],
)

if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")

    # Display uploaded file content
    st.subheader("Uploaded File Content")
    st.code(file_content, language="plaintext")

    # Analyze Button
    if st.button("🔍 Scan for Misconfigurations"):
        with st.spinner("Analyzing with AI-DevOps Guardian..."):
            analysis_result = analyze_with_gemini(file_content)
            if analysis_result:
                st.success("Analysis Complete!")
                st.subheader("🛠️ Misconfiguration Report")
                st.write(analysis_result)
else:
    st.info("Please upload a configuration file to begin analysis.")

# Footer
st.markdown("---")
st.markdown("🌟 Secure your DevOps with **AI-DevOps Guardian**")
