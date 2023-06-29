import streamlit as st

login = False
logout = False

def user_logout():
    del st.session_state['user']

def user_login():
    st.session_state['user'] = st.session_state['login_name']
    # st.sidebar.title(login_name)
    # return login_name

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
                    "PIN",type='password'
                    )
                login = login_form.form_submit_button(
                    "Log In",
                    on_click=user_login,
                    )
                if login:
                    st.session_state['user'] = login_form.login_name