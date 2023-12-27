import streamlit as st
import requests
import openai
import os
from get_news import News
from news_video import VideoGenerator
from dotenv import load_dotenv


load_dotenv()

news_api_key = os.getenv("NEWS_API_KEY")
news_client = News(api_key = news_api_key)

video_api_key = os.getenv("DID_API_KEY")
video_generator = VideoGenerator(video_api_key)

st.set_page_config(page_title="AI News Reporter",layout='wide')


st.title("The AI Newsroom")
st.markdown("<style>h1{color:orange;text-align:center}</style>",unsafe_allow_html=True)
st.subheader("Build with OpenAI,D-ID,Streamlit ❤️")
st.markdown("<style>h3{color:pink;text-align:center;font-size:15px}</style>",unsafe_allow_html=True)

image_url = st.text_input("Enter Image URL: ","")
query = st.text_input("Enter Query Keywords","")

num_of_news = st.slider("Number of News ",min_value=1,max_value=4,value=2)

if st.button("Generate"):
    if image_url.strip() and query.strip() and num_of_news is not None and num_of_news>0:
        col1,col2,col3 = st.columns([1,1,1])

        with col1:
            st.info("Your AI News Anchor : Alexa")
            st.image(image_url,caption='Anchor Image',use_column_width=True)

        with col2:
            desc_list =news_client.fetch_news_string(query,num_news=num_of_news)
            st.success("Your News is Fetched")
            st.write(desc_list)

        with col3:
            Intro_text  = f"""Hello Everyone, I'm Scarlet ,Welcome to the The AI Newsroom,your
            one-stop shop for all the latest news and information
            Here are the news :{desc_list}
            That's all fot today.Thank you and we hope that you will come back ofen
            for the latest news 
            """     
            video_url = video_generator.generate_video(Intro_text,image_url)

            st.warning("AI News Anchor Video")
            st.video(video_url)

    else:
        st.write("Failed to fetch news data. Please check your query and API Keys.")        

