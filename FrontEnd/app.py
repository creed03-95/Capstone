import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import Authentication
from utils.api import APIClient
from pages.chat import ChatPage

# Configure Streamlit page
st.set_page_config(
    page_title="Financial Advisor Dashboard",
    page_icon="💼",
    layout="wide"
)

def main():
    # Initialize authentication
    auth = Authentication()
    name, authentication_status, username = auth.authenticate()

    if authentication_status:
        # Sidebar for configuration
        with st.sidebar:
            st.title("Configuration")
            temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
            top_p = st.slider("Top P", 0.0, 1.0, 0.9, 0.1)
            st.write(f"Welcome, {name}")
            auth.logout()

        # Navigation (without "app" or "chat")
        selected = option_menu(
            menu_title=None,
            options=["Chat","Analytics", "Reports"],
            icons=["graph-up", "file-text"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )

        # Initialize API client
        api_client = APIClient()
        # Render selected page
        if selected == "Chat":
            chat_page = ChatPage(api_client, temperature, top_p)
            chat_page.initialize_session_state()
            chat_page.render(authentication_status)
        elif selected == "Analytics":
            st.title("Analytics")
            st.write("Analytics page coming soon...")
        elif selected == "Reports":
            st.title("Reports")
            st.write("Reports page coming soon...")

    elif authentication_status == False:
        st.error("Invalid username or password.")
    else:
        st.warning("Please login to access the dashboard.")


if __name__ == "__main__":
    main()