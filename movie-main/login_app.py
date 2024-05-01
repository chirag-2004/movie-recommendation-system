import streamlit as st
import mysql.connector

# Connect to the database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Yatendra@13",  # Replace with your actual password
    database="movie"
)
db_cursor = db_connection.cursor()

# Define function for login page
def login_page():
    st.write(
        """
        <style>
        
        
        .login-form {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .login-title {
            font-size: 24px;
            margin-bottom: 20px;
            color: #333333; /* Change text color */
        }
        .login-input {
            width: 300px;
            height: 40px;
            margin-bottom: 10px;
            padding: 5px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .login-button {
            width: 100%;
            height: 40px;
            margin-top: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write("<div class='login-form'>", unsafe_allow_html=True)
    st.write("<h2 class='login-title'>Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username", value="")
    password = st.text_input("Password", value="", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")

    st.write("</div>", unsafe_allow_html=True)

    
        


    

    def authenticate_user(username, password):
        query = "SELECT * FROM register WHERE username = %s AND password = %s"
        db_cursor.execute(query, (username, password))
        result = db_cursor.fetchone()
        if result:
            return True
        else:
            return False


