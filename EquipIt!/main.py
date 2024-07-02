# app.py
import streamlit as st


def main():
    st.title("My Streamlit Web App")

    # Add some content to your app
    st.write("Hello, this is a Streamlit web app!")

    # You can add interactive widgets
    user_input = st.text_input("Enter your name:")
    st.write(f"Hello, {user_input}!")


if __name__ == "__main__":
    main()

