import streamlit as st

login = False
logout = False

def user_logout():
    del st.session_state['user']

def user_login(login_name):
    st.session_state['user'] = login_name

def side_header():
    with st.sidebar:
        if 'user' in st.session_state:
            user = st.session_state['user']
            user_options = st.expander(str(user))
            with user_options:
                logout = st.button("Log Out",on_click=user_logout)
            if logout:
                del st.session_state['user']

        else:
            user_options = st.expander(
                "Not Signed In"
            )
            with user_options:
                login_form = st.form(
                    key='login_info',
                    clear_on_submit=True
                    )
                login_name = login_form.text_input("Username",value='jd')
                login_pin = login_form.number_input("PIN",min_value=0)
                login = login_form.form_submit_button(
                    "Log In",
                    kwargs={'login_name':login_name},
                    on_click=user_login
                    )