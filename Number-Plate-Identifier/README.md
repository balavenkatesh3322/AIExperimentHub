# Vehicle Details and Violation Detection

This project is a **vehicle details extraction** and **violation detection** application. It uses AI to analyze uploaded vehicle images, extract information such as the vehicle's number plate, model details, and check for safety violations (e.g., helmet absence).

## Features

- **Number Plate Detection:** Extracts the vehicle’s number plate from the image.
- **Vehicle Model Detection:** Identifies the vehicle type (car, bike, truck, etc.) and model or brand details.
- **Violation Detection:** Detects violations such as no helmet, overcrowding, or other safety infractions.
- **Image Processing:** Supports image formats like JPG, JPEG, and PNG.

## Requirements

To run this project locally, you'll need:

- Python 3.x
- Streamlit
- Pillow
- Google Generative AI API (for vehicle image analysis)

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies using `pip`:

    ```bash
    pip install streamlit pillow google-generativeai
    ```

3. Set up the **Google Generative AI API** by creating an account and obtaining an API key. Set the API key as an environment variable:

    ```bash
    export GEMINI_API_KEY="your-api-key-here"
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Upload a vehicle image (car, bike, or any vehicle).
3. The app will process the image, extract vehicle details, and check for safety violations like the absence of a helmet.

## Functionality

### **Vehicle Details Extraction:**
- Extracts the number plate number, vehicle type, and model details.
- Provides a clear, formatted output with all extracted information.

### **Violation Detection:**
- Identifies safety violations in the image, such as:
  - No helmet (for bikes).
  - Overcrowding.
  - Other visible violations.

## Example Output

```plaintext
Extracted Vehicle Information and Violations:

- Number plate number: ABC1234
- Vehicle type: Bike
- Vehicle model: Yamaha FZ
- Safety Violation: No helmet detected
