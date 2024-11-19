
import streamlit as st
import pandas as pd
from datetime import datetime

class ChatPage:
    def __init__(self, api_client, temperature, top_p):
        self.api_client = api_client
        self.temperature = temperature
        self.top_p = top_p                
        
    def initialize_session_state(self):
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
            
    def render(self, authentication_status):
        if not authentication_status:
            st.warning("You need to log in to access the Chat page.")
            return  # Exit early if the user is not authenticated
        
        # Render Chat UI
        st.title("AI Financial Advisor Chat")

        # Chat Interface
        st.markdown("### Chat")
        prompt = st.text_area("Enter your question:", height=100)

        if st.button("Submit"):
            if prompt:
                # Call API and get response
                response = self.api_client.chat_completion(prompt, self.temperature, self.top_p)

                # Save to session state
                st.session_state.chat_history.append({
                    'sno': len(st.session_state.chat_history) + 1,
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'prompt': prompt,
                    'response': response['response']
                })

                # Display the response
                st.markdown("### Response:")
                st.write(response['response'])

        # Chat History
        with st.expander("Chat History", expanded=True):
            if st.session_state.chat_history:
                df = pd.DataFrame(st.session_state.chat_history)
                st.dataframe(df, use_container_width=True)
            else:
                st.write("No chat history available.")
