import streamlit as st

# APP page settings
def page():
    st.set_page_config(
        page_title="Broken Link 404",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/SidneyTeodoroJr',
        'Report a bug': "https://github.com/SidneyTeodoroJr/broken_link_404",
        'About': "Contributions are welcome!"
        }
    )