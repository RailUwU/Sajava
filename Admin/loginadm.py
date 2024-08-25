import streamlit as st
import pyrebase
def app ():
    firebaseConfig = {

    'apiKey': "AIzaSyAj8xs1MSOfn4TR267Q4xxuVRixk-BQzIw",
    'authDomain': "cc-admin-93ecd.firebaseapp.com",
    'databaseURL': "https://cc-admin-93ecd-default-rtdb.firebaseio.com",
    'projectId': "cc-admin-93ecd",
    'storageBucket': "cc-admin-93ecd.appspot.com",
    'messagingSenderId': "725664768368",
    'appId': "1:725664768368:web:5889431478e84627736fb5",
    'measurementId': "G-6ZYG7JLH68"

    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Function to handle login logic
    def login(email, password):
        try:
            login = auth.sign_in_with_email_and_password(email, password)
            st.success("Successfully logged in!")
            # Implement actions after successful login (optional)
        except:
            st.error("Invalid email or password")

    # Function to handle signup logic
    def signup(email, password):
        try:
            user = auth.create_user_with_email_and_password(email, password)
            st.success("Account created successfully!")
            # Optionally ask for login after signup
        except:
            st.error("Email already exists")

    # Streamlit App Layout
    st.title("Login/Signup App")

    # Login Section
    email = st.text_input("Enter your email")
    password = st.text_input("Enter your password", type="password")

    if st.button("Login"):
        login(email, password)

    # Signup Section (optional)
    if st.checkbox("Sign up for a new account"):
        new_email = st.text_input("Enter new email")
        new_password = st.text_input("Enter new password", type="password")

        if st.button("Signup"):
            signup(new_email, new_password)
