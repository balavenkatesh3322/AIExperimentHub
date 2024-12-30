# AI-DevOps Guardian 🛡️

**AI-DevOps Guardian** is an AI-powered tool that scans your DevOps configuration files (e.g., Kubernetes YAML, Terraform, Dockerfiles, Ansible playbooks) for misconfigurations, security vulnerabilities, and best practice violations. The tool leverages **Google Gemini** to provide actionable remediation suggestions to enhance your DevOps security and performance.

## Features ✨

- **Upload Configuration Files** 📂: Supports multiple file formats including YAML, JSON, Dockerfile, and Terraform.
- **AI-Powered Analysis** 🤖: Utilizes **Google Gemini** to detect misconfigurations, security risks, and best practice violations in the uploaded files.
- **Remediation Suggestions** 🛠️: Provides actionable steps to fix detected issues.
- **User-Friendly Interface** 🌐: Built with Streamlit for easy interaction.

## Supported File Types 📝

- **Kubernetes YAML/Helm Charts**: e.g., `deployment.yaml`, `service.yaml`
- **Terraform Files**: e.g., `main.tf`, `variables.tf`
- **Dockerfile**: e.g., `Dockerfile`
- **Ansible Playbooks**: e.g., `site.yml`, `tasks/main.yml`
- **CloudFormation JSON**: e.g., `cloudformation-template.json`

## Requirements 🧰

- **Python 3.7+** 🐍
- **Google Gemini API Key** 🔑: Make sure to set up your Gemini API key in the `.env` file.

## 📝 How to Run the App Locally

```bash

- Clone this repository
- cd crop-disease-detection
- export GEMINI_API_KEY="your-api-key"
- pip install -r requirements.txt
- Run the Streamlit app: streamlit run app.py
```
Open your browser and go to localhost:8501 to use the app.


## How It Works ⚙️
1. Upload a File 📤: Upload a DevOps configuration file (e.g., Kubernetes YAML, Dockerfile).
2. Scan for Misconfigurations 🔍: AI scans the uploaded file for issues such as security risks, configuration mistakes, and performance bottlenecks.
3. Get Remediation Suggestions 📝: Receive AI-powered suggestions to fix any detected issues, ensuring best practices are followed.


## 🤝 Contributing
This project is open for contributions! Feel free to fork the repo and submit pull requests for new features, improvements, or bug fixes.

If you have any ideas for new features or enhancements, please create an issue to discuss them.

##  📢 Connect with Me
I welcome collaboration and discussions on this project. If you want to reach out, feel free to contact me:
LinkedIn

## License
This project is for educational and research purposes only.
