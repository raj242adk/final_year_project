import streamlit as st


def main():
    st.title("About Face Recognition App")

    # Add image
    st.image("face1.jpg", width=300)

    st.write("""
        This is a real-time attendance system using face recognition. 
        It identifies registered users and logs their attendance.
    """)

    st.subheader("How it Works")
    st.write("""
        1. **Registration**: Users register their faces along with their names and roles.
        2. **Real-time Recognition**: When a user shows their face to the camera, the app detects and identifies them in real-time.
        3. **Attendance Logging**: The app logs the attendance of recognized users.
    """)

    st.subheader("Meet the Team")
    st.write("""
        - Rabindra Adhikari
        - Ramdev Tamang
        - Chandra Laxmi Napit
    """)

    st.subheader("Contact Us")
    st.write("""
        If you have any questions or feedback, feel free to reach out to us at jamestamang544@gmail.com.
    """)


if __name__ == "__main__":
    main()
