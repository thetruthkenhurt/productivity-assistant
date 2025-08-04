# auth.py
import streamlit as st
from supabase import create_client, Client

SUPABASE_URL = "https://proassistant.streamlit.app/"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxvbHByZ3Ftc2J0Y3NkdHNjdnBhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjk0ODY3OTYsImV4cCI6MjA0NTA2Mjc5Nn0.GpyJxI_tnPtzfxsmQbttBjkdHGY8vRcTft3hTmviQFQ"

@st.cache_resource
def get_supabase_client():
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def login():
    st.subheader("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign in"):
        client = get_supabase_client()
        result = client.auth.sign_in_with_password({"email": email, "password": password})
        if result.user:
            st.session_state["user"] = result.user
            st.session_state["access_token"] = result.session.access_token
            st.success("Logged in successfully.")
            st.experimental_rerun()
        else:
            st.error("Login failed. Please check your credentials.")
