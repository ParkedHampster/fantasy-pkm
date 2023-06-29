import streamlit as st
import sqlite3 as sql
import pandas as pd

login = False
logout = False

def user_logout():
    del st.session_state['user']

def user_login():
    username = st.session_state['login_name']
    user_pin = st.session_state['login_pin']
    if len(user_pin) < 1:
        st.warning('Please input a PIN number')
        return
    try:
        user_pin = int(user_pin)
    except:
        st.warning('PIN numbers must be numbers')
        return
    with sql.connect("./data/users.db") as conn:
        cursor = conn.cursor()
        login_check = pd.read_sql(f"""
        SELECT * FROM logins
        WHERE LOWER( username ) = '{username.lower()}'
        """,conn)
    if int(user_pin) == login_check['pin'][0]:
        username = login_check['username'][0]
        st.session_state['user'] = username
        st.session_state['userID'] = login_check['userID'][0]

def side_header():
    with st.sidebar:
        if 'user' in st.session_state:
            user = st.session_state['user']
            user_options = st.expander(str(user))
            with user_options:
                logout = st.button("Log Out",on_click=user_logout)
        else:
            user_options = st.expander(
                "Not Signed In"
            )
            with user_options:
                login_form = st.form(
                    key='login_info',
                    clear_on_submit=True
                    )
                login_name = login_form.text_input(
                    "Username",
                    key='login_name'
                    )
                login_pin = login_form.text_input(
                    "PIN",type='password',
                    key='login_pin'
                    )
                login = login_form.form_submit_button(
                    "Log In",
                    on_click=user_login,
                    )

    # use this for testing and investigating session state
        # st.write(
        #     st.session_state
        # )