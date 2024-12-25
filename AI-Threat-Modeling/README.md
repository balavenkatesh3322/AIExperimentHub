# AI-Powered Threat Modeling Application

This project provides an AI-driven tool for analyzing threat modeling diagrams and offering recommendations for threat mitigation. It uses advanced generative AI models (such as Google Gemini) to analyze images of threat models and generate insights about potential threats, vulnerabilities, and mitigation strategies.

## Features

1. **Threat Modeling Analysis from Image Uploads**:
   - Users can upload threat modeling diagrams or architecture images in various formats (e.g., `.jpg`, `.png`, `.jpeg`).
   - The AI will analyze the uploaded diagram, identify potential threats and security issues, and generate mitigation strategies based on recognized patterns.

2. **Severity Classification for Each Threat**:
   - Each identified threat is classified based on its severity (e.g., Low, Medium, High).
   - The severity helps prioritize mitigation efforts by providing an understanding of how critical each threat is to the system.

3. **References for Mitigation**:
   - For each identified threat, the AI provides reference links to recognized standards and best practices (e.g., OWASP Top 10, STRIDE, NIST Cybersecurity Framework).
   - These resources help the user apply mitigation strategies and improve system security.

4. **Dynamic File Handling**:
   - The application dynamically generates temporary file names based on the uploaded image’s file extension.
   - Temporary files are automatically deleted after the image processing is complete to avoid any file system clutter.

5. **User-Friendly Interface**:
   - The application is built using Streamlit, providing an easy-to-use interface for uploading images and viewing analysis results.
   - A loading spinner appears while the AI processes the image, ensuring the user knows the system is working on the task.

6. **Output with Actionable Insights**:
   - The system generates detailed, actionable insights including the identification of threats, their severity, and mitigation strategies.
   - The results include links to detailed guides on how to address each specific issue.

## How to Use

### Step 1: Upload an Image
- Upload a threat modeling diagram or architecture image in `.jpg`, `.jpeg`, `.png`, or `.svg` format.
- The image will be processed using the AI model.

### Step 2: Wait for Processing
- The system will analyze the image and extract relevant information about potential threats and vulnerabilities in the diagram.
- While the analysis is running, a spinner will be shown to indicate that the system is processing the image.

### Step 3: View Results
- Once the analysis is complete, the system will display:
  - A list of identified threats.
  - The severity of each threat (Low, Medium, High).
  - Suggested mitigation strategies along with reference links to relevant resources for addressing each issue.

## Roadmap (Uncompleted Features)

Below are the planned features and improvements for the AI-Powered Threat Modeling application. These features will be implemented as part of future releases:

### 1. **Open Source LLM Integration**:
   - **Current Limitation**: The system currently uses Google Gemini for threat modeling analysis. We aim to integrate open-source large language models (LLMs) like `Llama2`, `GPT-3`, or `BLOOM` for cost-efficient and customizable deployment.
   - **Goal**: Provide flexibility in choosing an LLM model that best suits the user's needs.

### 2. **Additional Threat Detection Models**:
   - **Current Limitation**: The system primarily uses image-based analysis for threat modeling.
   - **Goal**: Integrate models that analyze network diagrams, data flow diagrams (DFD), and architecture diagrams in other formats (e.g., `.xml`, `.svg`).

### 3. **Custom Severity Levels**:
   - **Current Limitation**: The system uses basic severity levels (Low, Medium, High) for threats.
   - **Goal**: Allow customization of severity levels based on the specific context or risk analysis model used by the user (e.g., CVSS scores, NIST risk ratings).

### 4. **Multiple File Format Support**:
   - **Current Limitation**: The system supports limited image formats (e.g., `.jpg`, `.png`, `.jpeg`, `.svg`).
   - **Goal**: Expand support to other popular formats (e.g., `.pdf`, `.tiff`, `.bmp`) to accommodate a wider range of user inputs.

### 5. **Real-Time Threat Monitoring**:
   - **Current Limitation**: The system is limited to analyzing static images.
   - **Goal**: Integrate with real-time network or system monitoring tools to identify and analyze emerging threats dynamically in real-time environments.

### 6. **Collaborative Threat Modeling**:
   - **Current Limitation**: The application is limited to individual analysis.
   - **Goal**: Introduce multi-user collaboration features to allow teams to analyze threat models and share results within the app.

### 7. **Enhanced Report Generation**:
   - **Current Limitation**: The results are displayed on the interface.
   - **Goal**: Allow users to download detailed reports in various formats (e.g., PDF, Excel) summarizing the identified threats, severity, mitigation strategies, and references.

### 8. **Threat Model Database**:
   - **Current Limitation**: The application doesn't store user data.
   - **Goal**: Implement a database to store historical threat modeling data 


## Technologies Used

- **Streamlit**: For building the interactive web application.
- **Google Gemini**: For performing threat modeling analysis using generative AI (integration with other LLM models is planned).
- **PIL (Pillow)**: For image processing and handling.
- **Google Cloud**: For AI model hosting and processing.
- **Python**: For backend functionality.

## Installation Instructions

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/threat-modeling-ai.git
   cd threat-modeling-ai

2. pip install -r requirements.txt

3. export GEMINI_API_KEY="your-api-key"

5. streamlit run app.py

6. Open the application in your browser (usually at http://localhost:8501).

## Conclusion

This AI-Powered Threat Modeling application is a powerful tool for security professionals to analyze threat models and receive actionable insights for mitigating risks. The future roadmap includes integrations with open-source LLMs, enhanced customizability, and real-time monitoring features to create a robust security analysis platform.