import streamlit as st

def css():
    st.write("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,700;1,300&family=Poppins:wght@200&family=Roboto+Serif:ital,opsz,wght@1,8..144,200&display=swap');

    /*Removing the default menu button*/
    .stDeployButton {
        visibility: hidden;
    } 

    .st-emotion-cache-1vzeuhh {
        background-color: #ffffff;
    }

    /*Styling titles and text*/
    h1 {
        font-size: 2.3em;
    }

    h1, p {
        text-align: center;
    }

    p {
        font-size: 1.2em;
        
    }
    a {
        color: #ffffff;
    }
    #About {
        padding-top: 50%;
    }
    #logo {
        align-items: center;
    }
     img {
        border-radius: 50%;
        box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
    } 
<style/>
            """, unsafe_allow_html=True)