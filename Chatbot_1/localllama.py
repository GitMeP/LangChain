# Basic ChatBot to get response using OLLAMA - LLAMA2

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate  # ChatPromptTemplate-will provide the initial prompt template
from langchain_core.output_parsers import StrOutputParser # Default output parser whenever LLM gives response
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)


# Streamlit framework
st.title("Lanchain Demo with LLAMA2 API")
input_text=st.text_input("Search the topic you want")

# OpenaAI LLM
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

