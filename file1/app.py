import streamlit as st 

def clear_input_field():
    st.session_state.user_qution = st.session_state.user_input
    st.session_state.user_input='' 

def set_send_input():
    st.session_state.send_input = True
    clear_input_field()

def main(): 
    
    st.title('Multimodel local Chat App')
    chat_container = st.container()

    if 'send_input' not in st.session_state:
        st.session_state.send_input= False
        st.session_state.user_qution = ''

    user_input = st.text_input('type your message here', key='user_input', on_change =set_send_input)

    send_button = st.button('Send', key='send_button')

    if send_button or st.session_state.send_input:
        if st.session_state.user_qution != '':
            llm_response = 'This is a response from LLM model'
            with chat_container:
               st.chat_message('user').write(st.session_state.user_qution)   
               st.chat_message('ai').write('here is an answer')

if __name__ == '__main__':
    main()

