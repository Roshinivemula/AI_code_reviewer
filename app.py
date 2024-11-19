import streamlit as st
import google.generativeai as ai

f = open("D:\\innomatics\\keys\\Api_keys.txt")
key = f.read()
ai.configure(api_key = key)

sys_prompt = """You are a helpful AI Tutor as a Code Reviwer for python programming.
Students will give you code snippet in python, your task is to review and receive feedback on potential bugs along with suggestions for fixes. 
You should be efficient, and provide accurate bug reports and fixed code snippets.
In case if a student ask any question outside the python scope, politely decline and tell them to ask the question from python only."""

model = ai.GenerativeModel(model_name="models/gemini-1.5-pro",system_instruction=sys_prompt)


st.title("_Python_ - :blue[AI code Reviwer]")

user_prompt = st.text_area("Enter your Python code here:")

btn_click = st.button("Review code")

if btn_click == True:
    response = model.generate_content(user_prompt)
    st.write(response.text)


