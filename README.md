Employee Salary Prediction AI
This project is a Streamlit-based web application that predicts whether an employee's income is likely to be more than $50K or not, based on demographic and work-related inputs. It includes both real-time single predictions and batch predictions using CSV uploads. Additionally, the application provides optional voice input functionality for a more interactive user experience.

Features
Single Employee Salary Prediction
Enter employee details manually or through voice input and predict whether their income is above or below $50K.

Batch Prediction from CSV
Upload a CSV file with employee records and predict the salary class for each entry in a tabular format.

Speech Recognition (Optional)
Users can use microphone input to fill in data for fields like age, education, occupation, and working hours.

Machine Learning Model
The app uses a trained RandomForestClassifier model to make predictions, based on a cleaned version of the adult.csv dataset.

Model Accuracy Display
Displays training accuracy of the model to inform users about the prediction quality.

Tech Stack
Python 3.8+

Pandas

NumPy

Scikit-learn

Streamlit

SpeechRecognition (Google API)

Dataset
The app uses the UCI Adult Dataset which contains demographic data used to predict income levels (>50K or ≤50K). The dataset is preprocessed to remove null values and encode categorical features.

Key features used:

Age

Education

Occupation

Hours-per-week

Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/yourusername/salary-prediction-ai.git
cd salary-prediction-ai
Create and Activate Virtual Environment

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
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
File Structure
bash
Copy
Edit
salary-prediction-ai/
│
├── app.py                  # Main Streamlit application
├── adult.csv               # Dataset used for training
├── requirements.txt        # List of required Python libraries
└── README.md               # Project documentation
Voice Input Instructions
Enable microphone access in your browser.

Click the checkbox Use Voice Input to activate speech recognition.

Speak the values clearly when prompted:

Age (number)

Education (e.g., Bachelors, HS-grad)

Occupation (e.g., Tech-support, Sales)

Hours-per-week (number)

If speech input fails, the app allows fallback to manual entry.

Input Requirements for CSV Upload
Your CSV file must contain the following column names:

age

education

occupation

hours-per-week
