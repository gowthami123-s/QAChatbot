import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv("/Users/maramgowthami/Documents/Langchain/.env")

groq_api_key=os.getenv("GROQ_API")


prompt=ChatPromptTemplate.from_messages(
    
    [("system","Your are an. helpful assistant answer to the following question"),
     ("user","question:{question}")
     
   ]
)

def generate_response(api_key,model,question,temp,max_tokens):
    model=ChatGroq(model=model,groq_api_key=api_key) 
    output_parser=StrOutputParser()
    chain=prompt|model|output_parser
    reponse=chain.invoke({"question":question})
    return reponse


## Build the application

st.title("Simple QA Chatbot")

st.sidebar.title("Settings")

api_key=st.sidebar.text_input("Enter the password for api key",type="password")

model=st.sidebar.selectbox("Select an open AI model",["openai/gpt-oss-20b","gpt-oss-10b"])
temp=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=0.0,max_value=1.0,value=0.5)
st.write("Go ahead and ask any question")

user_input=st.text_input("You:")

if user_input:
    reponse=generate_response(api_key,model,user_input,temp,max_tokens)
    st.write(reponse)

else:
    st.write("Please provide the query")
    
    





