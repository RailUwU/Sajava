import streamlit as st
from streamlit_option_menu import option_menu
import home, forums, events, chatbot, loginstu

# Set up the page configuration
st.set_page_config(
    page_title="CollegeConnect",
    page_icon="cc.png"
)

# Define the MultiApp class
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Create the sidebar menu using option_menu
        with st.sidebar:        
            app = option_menu(
                menu_title='CollegeConnect',
                options=['Home', 'Forums', 'Events', 'Chatbot', 'Login/Signup'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"}, 
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        
        # Clear the main area before rendering the selected page
        st.empty()

        # Run the selected app function
        if app == "Home":
            home.app()
        elif app == "Forums":
            forums.app()    
        elif app == "Events":
            events.app()        
        elif app == 'Chatbot':
            chatbot.app()
      
        elif app == 'Login/Signup':
             loginstu.app()    

# Create an instance of the MultiApp class and run it
multi_app = MultiApp()
multi_app.run()
