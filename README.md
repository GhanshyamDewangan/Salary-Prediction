Employee Salary Prediction AI
A Streamlit-based web application that predicts whether an employee's income is likely to exceed $50K annually, based on demographic and occupational attributes. The application supports real-time predictions, batch predictions via CSV uploads, and optional voice input for interactive use.

🧠 Introduction
This AI-powered tool leverages a trained RandomForestClassifier on the UCI Adult Dataset to classify whether an individual's salary is > $50K or ≤ $50K. It provides both manual and voice-assisted input options, making it accessible and interactive. The application also supports batch processing for evaluating multiple records via CSV files.

📑 Table of Contents
Features

Tech Stack

Dataset

Installation

Usage

Voice Input Instructions

Input Requirements for CSV Upload

File Structure

Troubleshooting

Contributors

License

✨ Features
Single Employee Salary Prediction
Manually enter details or use voice input to predict whether the salary exceeds $50K.

Batch Prediction from CSV
Upload a CSV file containing multiple employee records and view predictions in a table.

Speech Recognition (Optional)
Users can fill in fields like age, education, occupation, and working hours using their voice.

Machine Learning Model
Uses a trained RandomForestClassifier on a preprocessed version of the UCI Adult dataset.

Model Accuracy Display
Real-time display of model training accuracy for user confidence.

🧰 Tech Stack
Python 3.8+

Pandas

NumPy

Scikit-learn

Streamlit

SpeechRecognition (Google Speech API)

📊 Dataset
This application uses the UCI Adult Dataset, a public dataset from the UCI Machine Learning Repository that includes demographic data used to predict income level.

Key features used:
age

education

occupation

hours-per-week

All data is cleaned: missing values are removed, and categorical features are encoded.

⚙️ Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/salary-prediction-ai.git
cd salary-prediction-ai
Create and Activate a Virtual Environment

bash
Copy
Edit
# For Linux/Mac
python -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.venv\Scripts\activate
Install Required Libraries

bash
Copy
Edit
pip install -r requirements.txt
Run the Application

bash
Copy
Edit
streamlit run app.py
🚀 Usage
Once the app launches in your browser:

Choose between Single Prediction or Batch Prediction.

Enter employee details manually or opt for Voice Input.

For batch predictions, upload a correctly formatted CSV file.

View model accuracy and prediction results in real time.

🎙️ Voice Input Instructions
To use voice input:

Ensure microphone access is enabled in your browser.

Check the "Use Voice Input" box in the app.

Speak clearly when prompted for:

Age (e.g., "thirty-five")

Education (e.g., "Bachelors")

Occupation (e.g., "Sales")

Hours-per-week (e.g., "forty")

If speech input fails, manual entry will still be available.

📂 Input Requirements for CSV Upload
Your CSV file must contain the following column headers (case-sensitive):

csv
Copy
Edit
age,education,occupation,hours-per-week
Each row should represent one employee record.

🗂️ File Structure
bash
Copy
Edit
salary-prediction-ai/
│
├── app.py                  # Main Streamlit application
├── adult.csv               # Dataset used for training
├── requirements.txt        # List of required Python libraries
└── README.md               # Project documentation
🛠️ Troubleshooting
Speech Recognition Not Working?

Ensure your browser has microphone access.

Use Chrome or Edge for best compatibility.

Fallback to manual entry if speech input fails.

Streamlit App Not Launching?

Check your Python version (must be 3.8+).

Reinstall packages: pip install -r requirements.txt.

CSV Upload Fails?

Ensure the file includes the correct column headers and data types.

