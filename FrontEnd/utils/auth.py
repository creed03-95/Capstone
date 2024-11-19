# utils/auth.py
import streamlit as st
import yaml
import streamlit_authenticator as stauth

class Authentication:
    def __init__(self):
        # Load the configuration file
        with open('config/auth_config.yaml') as file:
            self.config = yaml.safe_load(file)
        
        # Create the authenticator object with updated method
        self.authenticator = stauth.Authenticate(
            credentials=self.config['credentials'],
            cookie_name=self.config['cookie']['name'],
            key=self.config['cookie']['key'],
            cookie_expiry_days=self.config['cookie']['expiry_days']
        )

    def authenticate(self):
        # Updated login method with new parameter 'fields'
        try:
            login_status = self.authenticator.login(
                fields=['username', 'password'],
                location='main'
            )
            
            # Unpack the login status
            if login_status:
                # Check authentication status
                if st.session_state["authentication_status"]:
                    return (
                        st.session_state["name"], 
                        st.session_state["authentication_status"], 
                        st.session_state["username"]
                    )
                elif st.session_state["authentication_status"] is False:
                    st.error('Username/password is incorrect')
                    return None, False, None
                elif st.session_state["authentication_status"] is None:
                    st.warning('Please enter your username and password')
                    return None, None, None
            
            return None, None, None
        
        except Exception as e:
            st.error(f"An error occurred during authentication: {e}")
            return None, None, None

    def logout(self):
        # Updated logout method
        self.authenticator.logout('Logout', 'main', key='unique_key')

import bcrypt
import yaml

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

# Example usage
passwords = {
    'admin': 'admin_password',
    'advisor': 'advisor_password',
    'analyst': 'analyst_password'
}

# Load existing config
with open('config/auth_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Update passwords
for username in config['credentials']['usernames']:
    if username in passwords:
        config['credentials']['usernames'][username]['password'] = hash_password(passwords[username])

# Save updated config
with open('config/auth_config.yaml', 'w') as file:
    yaml.dump(config, file)

print("Passwords updated successfully!")