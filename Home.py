import streamlit as st

from shared_code.user_status import side_header

def user_logout():
    del st.session_state['user']
# login = st.button("Log In")

tmp_uname = st.text_input("TMP - Set Username")
t_uname = st.button("TEST UNAME")

if t_uname:
    st.session_state['user'] = tmp_uname

# login = False
# logout = False

side_header()
# with st.sidebar:
#     if 'user' in st.session_state:
#         user = st.session_state['user']
#         user_options = st.expander(str(user))
#         with user_options:
#             logout = st.button("Log Out",on_click=user_logout)
#         if logout:
#             del st.session_state['user']

#     else:
#         user_options = st.expander(
#             "Not Signed In"
#         )
#         with user_options:
#             login_name = st.text_input("Username")
#             login_pin = int(st.number_input("PIN",min_value=0))
#             login = st.button("Log In")
#         if login:
#             st.session_state['user'] = login_name
