import streamlit as st
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
import datetime
from PIL import Image
from ml_model.model import predict_dental_issues
from ml_model.diagnosis_utils import diagnosis_and_treatment
from models import Child, Scan, Visit, HygieneReport, UserSession


# Load environment variables
load_dotenv()

# Firebase Configuration
firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "appId": os.getenv("FIREBASE_APP_ID")
}

# Pyrebase Auth Init
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Firebase Admin SDK Init (for Firestore)
service_account_path = os.getenv("SERVICE_ACCOUNT_KEY_PATH")
if not service_account_path or not os.path.exists(service_account_path):
    st.error("SERVICE_ACCOUNT_KEY_PATH environment variable is not set or the file does not exist.")
    st.stop()
cred = credentials.Certificate(service_account_path)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()


# Streamlit UI
st.set_page_config(page_title="CavityCam+", layout="centered")
st.title("🦷 CavityCam+ - AI Dental Guardian")

# Auth: Sign Up / Log In
auth_mode = st.sidebar.radio("Account", ["Login", "Sign Up"])

email = st.sidebar.text_input("Email")
password = st.sidebar.text_input("Password", type="password")

if auth_mode == "Sign Up":
    if st.sidebar.button("Create Account"):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Account created. You can now log in.")
        except Exception as e:
            st.error("Error creating account.")
            st.write(e)
elif auth_mode == "Login":
    if st.sidebar.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success("Logged in successfully!")
        except:
            st.error("Invalid credentials")

# Logout
if "user" in st.session_state:
    if st.sidebar.button("Logout"):
        st.session_state.pop("user")
        st.success("Logged out.")
        st.stop()

# Main App 
if "user" in st.session_state:
    user_email = st.session_state.user['email']
    st.sidebar.success(f"Logged in as {user_email}")

    st.subheader("👶 Add Child Profile")
    child_name = st.text_input("Child Name")
    child_age = st.number_input("Age", min_value=1, max_value=15)
    uploaded = st.file_uploader("Upload Tooth Image", type=["jpg", "png", "jpeg"])

    if st.button("Submit Scan"):
        if child_name and uploaded:
            image = Image.open(uploaded)
            predictions = predict_dental_issues(image)
            results_display = "\n".join([f"{k}: {v}" for k, v in predictions.items()])

            child = Child(name=child_name, age=child_age)
            scan = Scan(
                email=user_email,
                child=child,
                image_name=uploaded.name,
                predictions=predictions,
                date=datetime.datetime.now()
            )
            db.collection("scans").add(scan.to_dict())
            st.success("Scan uploaded and analyzed!")

            st.image(image, caption="Tooth Scan", width=250)
            st.markdown("### 🧠 AI Risk Assessment")
            for issue, data in predictions.items():
                if data["detected"]:
                 st.markdown(f"### 🚨 {issue} Detected")
                 details = diagnosis_and_treatment(issue, child_age)
                 st.markdown(f"- **Cause:** {details['cause']}")
                 st.markdown(f"- **Prevention:** {details['prevention']}")
                 st.markdown(f"- **Treatment:** {details['treatment']}")
                 st.markdown(f"- **Age Advice:** {details['age_note']}")
                else:
                 st.markdown(f"✅ **{issue}**: Not Detected")
        else:
            st.warning("Enter details and upload an image.")

    st.subheader("📜 Your Scan History")
    user_scans = db.collection("scans").where("email", "==", user_email).stream()
    for doc in user_scans:
        scan = doc.to_dict()
        prediction_result = scan.get("predictions", {})
        st.write(f"{scan['date'].strftime('%Y-%m-%d')} - {scan['child_name']}")
        for issue, res in prediction_result.items():
            st.markdown(f"• **{issue}**: {res}")
        st.markdown("---")

  # Visit Tracking Feature
    st.subheader("📅 Dental Visit Tracker")
    with st.form("visit_form"):
        visit_date = st.date_input("Next Visit Date")
        reason = st.text_input("Visit Reason")
        submitted = st.form_submit_button("Save Visit")
        if submitted:
            visit = Visit(
                email=user_email,
                visit_date=datetime.datetime.combine(visit_date, datetime.datetime.min.time()),
                reason=reason
            )
            db.collection("visits").add(visit.to_dict())
            st.success("Visit scheduled.")

    st.subheader("📆 Upcoming Visits")
    visits = db.collection("visits").where("email", "==", user_email).stream()
    for doc in visits:
        visit = doc.to_dict()
        st.write(f"📌 {visit['visit_date'].strftime('%Y-%m-%d')} - Reason: {visit['reason']}")

 # Gamified Hygiene Tracker
    st.subheader("🎮 Daily Dental Hygiene Challenge")
    today = datetime.datetime.now().date().isoformat()
    brushed = st.checkbox("Brushed Teeth Today")
    flossed = st.checkbox("Flossed Today")

    if st.button("Submit Hygiene Report"):
        hygiene = HygieneReport(
            email=user_email,
            child_name=child_name,
            date=today,
            brushed=brushed,
            flossed=flossed
        )
        db.collection("hygiene_reports").add(hygiene.to_dict())
        st.success("Hygiene report submitted!")

    st.subheader("📈 Hygiene Progress")
    hygiene_docs = db.collection("hygiene_reports").where("email", "==", user_email).stream()
    for doc in hygiene_docs:
        hygiene = doc.to_dict()
        status = "✅" if hygiene['brushed'] and hygiene['flossed'] else "⚠️"
        st.write(f"{hygiene['date']} - {hygiene['child_name']} - {status}")