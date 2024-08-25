import streamlit as st

def app():
    # Display the main image and title
    st.image("cc.png", width=250)
    st.title("College Connect")

    # Add a brief description of the application
    st.markdown("""
        \"CollegeConnect\" is an AI chatbot that centralizes information for Rajasthan's engineering and polytechnic institutes.
        - Availability: 24/7 real-time answers on admissions, fees, scholarships, and more.
        - NLP Support: Understands English; potential for other languages
        - User Experience: Intuitive interface with data-driven insights for optimization.
        - Efficiency: Automates common queries, reduces staff workload, and ensures consistent, up-to-date information.
        - Accessibility: Provides easy, round-the-clock access, removing the need for direct college contact.
    """)
