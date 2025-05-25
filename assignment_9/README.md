🦷 CavityCam+ – AI Dental Guardian for Families

CavityCam+ is an AI-powered Streamlit web application designed to assist parents in monitoring their children’s oral health. Users can upload intraoral photos, and the app detects early dental issues like cavities, plaque, discoloration, and malalignment using machine learning. It includes features for tracking hygiene habits, dentist visits, and storing dental records.

---

Features Implemented (v1)

Authentication: Sign-up, login, and session handling using Firebase Authentication.
Child Profile + Scan Upload: Upload intraoral images and associate them with a child's profile.
AI Diagnosis: Automatically detects:
  Cavities
  Discoloration
  Plaque/Swelling
  Malalignment
Visit Tracker: Log upcoming dentist appointments with reason and date.
Gamified Hygiene Tracker: Track daily brushing and flossing with progress monitoring.
Cloud Firestore: All scans, reports, and visits stored securely via Firebase Firestore.
Python OOP: Models used to encapsulate business logic (`Child`, `Scan`, `Visit`, `UserSession`, etc.)
Business Model Integrated: Monetization strategy outlined in product vision.

---

Business Vision (Future Additions)

| Feature | Description | Monetization |
|--------|-------------|---------------|
|  Teledentistry | Consult dentist online post-AI detection | Rs. 100–500/consult |
|  Multi-child profiles | Parents can manage multiple kids | Freemium features |
|  Product Recommender | Fluoride toothpaste, floss, etc. | Affiliate sales |
|  School Portal | Mass AI screenings for students | SaaS for schools/NGOs |
|  Dental Vault | Store/share records securely | Subscription model |

---

Tech Stack

Frontend: Streamlit
Backend: Firebase (Auth + Firestore)
ML: Custom-trained AI model for dental issue classification (`ml_model`)
Storage: Firebase Storage (planned)
Payments: Stripe / JazzCash (in progress)
Environment Management: `python-dotenv`

---



