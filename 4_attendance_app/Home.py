import streamlit as st
import cv2
import face_rec
st.set_page_config(page_title="Fast Face Recognition System", layout="wide")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;'>Fast Face Recognition System</h1>", unsafe_allow_html=True)
st.markdown("""---""")
st.markdown("<h2 style='color: DodgerBlue'>Clock In with a Smile: Let Your Face be  Recognized!</h2>", unsafe_allow_html=True)

st.image('face1.jpg', use_column_width=True)

st.markdown("<p>Face recognition attendance systems work by using computer vision algorithms to identify and verify individuals based on their facial features.</p>", unsafe_allow_html=True)

footer_container = st.container()

with footer_container:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Mission")
        st.markdown("<h4>this is the mission of projects!</h4>", unsafe_allow_html=True)

    with col2:
        st.header("Contact")
        css_example = """
               <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
               <i class="fa-sharp fa-solid fa-envelope"></i>ram@gmail.com</p>
               <i class="fa-solid fa-mobile"></i>+(977) 98098765</p>
               <i class="fa-solid fa-location-dot"></i> chabahil, gangahitti, KTM

               """
        st.write(css_example, unsafe_allow_html=True)

    with col3:

        st.header("Social Media")
        st.markdown("""
                   <i class="fab fa-instagram" style="font-size:24px;"></i>&nbsp;&nbsp;&nbsp;
                   <i class="fab fa-twitter" style="font-size:24px;"></i>&nbsp;&nbsp;&nbsp;
                   <i class="fab fa-youtube" style="font-size:24px;"></i>
                   """,
                unsafe_allow_html=True)
