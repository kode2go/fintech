import streamlit as st

def about():
    st.title('Founder')
    with st.container():
        col1,col2=st.columns(2)
        col1.write('')
        col1.write('')
        col1.write('')
        col1.write('**Name:**    Kossi Toulassi')
        col1.write('**Education:**     Chartered Accountant (CA)')
        col1.write('**Experience:**     18+ years of experience in the public and private sector')
        col1.write('**Contact:**    k.toulassi@gmail.com or [linkedin](https://www.linkedin.com/in/kossi-toulassi/)')
        col1.write('**Thanks for stopping by!**')
        col2.image('kossi.png')
