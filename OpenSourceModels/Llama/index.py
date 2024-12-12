import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate


## function to get responce from LLAma 2 model


def getLLamaresponse(input_text ,no_words , blog_style):

    ## LLma Model

    llm = CTransformers(
    model="Models/llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_type="llama",  # Try using gpt if llama doesn't work
    config={
        'max_new_tokens': 256,
        'temperature': 0.01
    }
    )   
    
    ## Prompt Template
    template = """
        Write a blog for {blog_style} for a topic {input_text} with in 
        {no_words} words.
    """
    prompt_template = PromptTemplate(
        input_variables = ["blog_style","input_text","no_words"],
        template = template
    )

    ###GEnerate the responce from the LLama 2 model

    response = llm(prompt_template.format(blog_style = blog_style , input_text = input_text , no_words = no_words))


    return response













st.set_page_config(page_title="Generate Blogs" ,
                    page_icon=":)",
                    layout="centered",
                    initial_sidebar_state="collapsed")

st.header("Generate my Blogs :) ")

input_text = st.text_input("Enter your text", "")


## creating to more columns for additional 2 fields

col1 , col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words ")

with col2:
    blog_style =st.selectbox("Writing the blog for ", ["Technology", "Finance", "Sports"],index=0)


submit = st.button("Generate")

if submit:
    st.write( getLLamaresponse(input_text,no_words,blog_style))
