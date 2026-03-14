import streamlit as st
st.title('Form')
with st.form(key='form'):
    name=st.text_input("Enter your name: ")
    age= st.number_input("Enter your height: ")
    gender= st.selectbox("Gender",["male","female"])
    
    submit=st.form_submit_button()
    if(submit):
        if (name=="" or age=="" or gender=="" ):
            st.warning("Please fill the form properly")
        else:
            st.balloons()
        


