import openai
import streamlit as st
from PIL import Image

def load_image(img):
    im=Image.open(img)
    return im
size=20

st.markdown("<h1 style='text-align: center;'>OpenCode 💬</h1>", unsafe_allow_html=True)
st.markdown("---")
with st.sidebar:
    st.image("F:/OpenCode-main/OpenCode-main/ai.jpeg")
    st.title("OpenSolution")
    st.caption('''
    OpenSolution aims to provide solution of any College and School Level question according to the user needs. OpenSolution is developed for the students struggling while learning.
    ''', unsafe_allow_html=False)
   

platform=st.selectbox("Select the Platform of Question:", ("quickmath", "englishtestsonline", "futurelearn"))
language=st.selectbox("Select the Subject of Solution:", ("English", "Mathematics", "Science"))
ques=st.text_area("Input the Question Here")
button=st.button("Generate")



def gen_auto_response(ques):
    openai.api_key=st.secrets["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"]
    
    response = openai.Completion.create(
        model="code-cushman-001",
        prompt=f""""Given a Mathematics solution for the quickmath question below
                    {platform} Question: {ques}
                    {language} Solution: """,
        temperature=0,
        max_tokens=1114,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    print(response)
    return response.choices[0].text

if ques and button:
    with st.spinner("-------Generating Solution------"):
        reply=gen_auto_response(ques)
        st.code(reply)
        
        button2=st.button("Explain Solution")
        






