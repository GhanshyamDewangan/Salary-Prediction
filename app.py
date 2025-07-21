import pandas as pd
import numpy as np
import streamlit as st
import speech_recognition as sr
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Page config
st.set_page_config(page_title="Employee Salary Predictor", layout="wide")

# Title
st.title(" Salary Prediction AI")
st.write("Predict Salary with the help of CSV files or Dataset's")

# Custom styling for checkbox and warning message
st.markdown("""
    <style>
        div.row-widget.stCheckbox > div {
            font-size: 18px;
        }
        .big-warning {
            color: red;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("adult.csv")
    df.dropna(inplace=True)
    df['income'] = df['income'].apply(lambda x: 1 if '>50K' in str(x) else 0)
    return df

df = load_data()

# Label encode categorical columns
le_edu = LabelEncoder()
le_job = LabelEncoder()
df['education'] = le_edu.fit_transform(df['education'])
df['occupation'] = le_job.fit_transform(df['occupation'])

# Train model
X = df[['age', 'education', 'occupation', 'hours-per-week']]
y = df['income']
model = RandomForestClassifier()
model.fit(X, y)
accuracy = accuracy_score(y, model.predict(X))

# Function for speech recognition
def recognize_speech(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(f" {prompt} (Speak Now)")
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.warning("Could not understand audio.")
        except sr.RequestError:
            st.error("Speech Recognition request failed.")
    return ""

# UI Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Enter Employee Information")

    use_voice = st.checkbox("🎙 Use Voice Input")

    # Default values
    age = 30
    education = le_edu.classes_[0]
    occupation = le_job.classes_[0]
    hours = 40

    if use_voice:
        voice_failed = False  # Flag for tracking

        age_input = recognize_speech("Enter Age")
        if age_input and age_input.isdigit():
            age = int(age_input)
        else:
            voice_failed = True

        education_input = recognize_speech("Enter Education (e.g., Bachelors, HS-grad)")
        if education_input in le_edu.classes_:
            education = education_input
        else:
            voice_failed = True

        occupation_input = recognize_speech("Enter Occupation (e.g., Tech-support, Sales)")
        if occupation_input in le_job.classes_:
            occupation = occupation_input
        else:
            voice_failed = True

        hours_input = recognize_speech("Enter Working Hours per Week")
        if hours_input and hours_input.isdigit():
            hours = int(hours_input)
        else:
            voice_failed = True

        # Show message only if something failed
        if voice_failed:
            st.markdown(
                "<div class='big-warning'> Voice input failed. You can still fill manually.</div>",
                unsafe_allow_html=True
            )

    # Manual fallback input
    age = st.slider("Age", 18, 70, age)
    education = st.selectbox("Education Level", le_edu.classes_, index=list(le_edu.classes_).index(education))
    occupation = st.selectbox("Occupation Type", le_job.classes_, index=list(le_job.classes_).index(occupation))
    hours = st.slider("Working Hours Per Week", 10, 100, hours)

    # Encode inputs for prediction
    edu_enc = le_edu.transform([education])[0]
    job_enc = le_job.transform([occupation])[0]
    input_data = np.array([[age, edu_enc, job_enc, hours]])

    if st.button(" Predict"):
        prediction = model.predict(input_data)[0]
        result = ">50K" if prediction == 1 else "≤50K"
        st.success(f"**Predicted Salary Class:** {result}")
        st.info(f" Model Accuracy: {round(accuracy * 100, 2)}%")

with col2:
    st.subheader("📁 Batch Prediction Using CSV")

    file = st.file_uploader("Upload CSV File", type=["csv"])

    if file:
        try:
            df_batch = pd.read_csv(file)
            df_batch['education'] = le_edu.transform(df_batch['education'])
            df_batch['occupation'] = le_job.transform(df_batch['occupation'])

            batch_X = df_batch[['age', 'education', 'occupation', 'hours-per-week']]
            preds = model.predict(batch_X)
            df_batch['Predicted Income'] = ['>50K' if p == 1 else '≤50K' for p in preds]

            st.write("Batch Prediction Results:")
            st.dataframe(df_batch)
        except Exception as e:
            st.error(" Error in CSV file. Ensure columns: age, education, occupation, hours-per-week.")
