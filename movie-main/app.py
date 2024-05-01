import streamlit as st
import json
from Classifier import KNearestNeighbours
from operator import itemgetter
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import mysql.connector
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from login_app import login_page



sid = SentimentIntensityAnalyzer()

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Yatendra@13",
    database="movie"
)
db_cursor = db_connection.cursor()



img = Image.open('./images/favicon.png')
st.set_page_config(page_title='Movie Recommender Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")

    
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
                background-color:#a873b0;
                font-size:12px;
                font-weight:5px;
                height:30px;
                margin:1rem;
                padding:0.8rem;
                content:'Copyright © 2022 : Pragya Bisherwal';
                display: flex;
                align-items:center;
                justify-content:center;
                color:white;
            }
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
lottie_contact =load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dhcsd5b5.json")
lottie_loadLine =load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yyjaansa.json")
lottie_Login =load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_S6vWEd.json")



with st.sidebar:
    selected = option_menu(
                menu_title="MOVIES MANIA",  
                options=["Home", "About", "Login"], 
                icons=["house", "person-square", "login"],  
                menu_icon="cast",  
                default_index=0,  
                 styles={
                "container": {"padding": "5!important", "background-color": "#0E1117" , "Font-family":"Monospace"},
                "icon": {"color": "#A0CFD3", "font-size": "25px"}, 
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px","Font-family":"Monospace"},
                "nav-link-selected": {"background-color": "#90EE90"},
                }
                )

    if selected == "Home":
      st.empty()
    
    if selected == "About":
        st.markdown("""
        <div style='
            background-color:#a873b0; 
            padding:1rem;
            font-size:17px;
            border-radius:8px;
            text-align: justify;
           '>
            We are a group of 4 Enthusiastic Students from 2nd Year CSE-DS ABESEC who are on our way to embark on a journey of Technological Excellence in the Near Future.
        </div>
        <br>
       """
        ,unsafe_allow_html=True,)

        
        st.subheader("Visit our LinkedIn Profiles 💻")
        st.markdown(
            """
            <div style='
            background-color:#A0CFD3; 
            font-weight:bold;
            cursor:pointer; 
            height:2.8rem;
            font-size:20px;
            border-radius:10px;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
            display: flex;
            align-items:center;
            justify-content:center;'>
                    <a  href="https://www.linkedin.com/in/devansh-vashishtha/" 
                    style='color: white; 
                           text-decoration:none;
                           padding-top:6px;
                           color: black; 
                           padding-bottom:5px;
                           text-align:center;'>
                           Devansh Vashishtha 👨‍💻 
                    </a>    
            
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        
        st.markdown(
            """
            <div style='
            background-color:#A0CFD3; 
            font-weight:bold;
            cursor:pointer; 
            height:2.8rem;
            margin-top : 25px;
            font-size:20px;
            border-radius:10px;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
            display: flex;
            align-items:center;
            justify-content:center;'>
                    <a  href="https://in.linkedin.com/in/deepak-yadav-12ba4a258" 
                    style='color: white; 
                           text-decoration:none;
                           padding-top:6px;
                           color: black; 
                           padding-bottom:5px;
                           text-align:center;'>
                           Deepak Yadav 👨‍💻 
                    </a>    
            
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        
        
        st.markdown(
            """
            <div style='
            background-color:#A0CFD3; 
            font-weight:bold;
            cursor:pointer; 
            height:2.8rem;
            margin-top : 25px;
            font-size:20px;
            border-radius:10px;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
            display: flex;
            align-items:center;
            justify-content:center;'>
                    <a  href="https://www.linkedin.com/in/chirag-gupta-86a9262a2" 
                    style='color: white; 
                           text-decoration:none;
                           padding-top:6px;
                           color: black; 
                           padding-bottom:5px;
                           text-align:center;'>
                           Chirag Gupta 👨‍💻 
                    </a>    
            
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        
        
        st.markdown(
            """
            <div style='
            background-color:#A0CFD3; 
            font-weight:bold;
            cursor:pointer; 
            height:2.8rem;
            margin-top : 25px;
            font-size:20px;
            border-radius:10px;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
            display: flex;
            align-items:center;
            justify-content:center;'>
                    <a  href="https://www.linkedin.com/in/bharat-singhal-1105452a5/" 
                    style='color: white; 
                           text-decoration:none;
                           padding-top:6px;
                           color: black; 
                           padding-bottom:5px;
                           text-align:center;'>
                           Bharat Singhal👨‍💻 
                    </a>    
            
            </div>
            """,
            unsafe_allow_html=True,
        )
            
    if selected == "Login":
        login_page()
        

        
        
        
        
        

def get_similar_movies(selected_movie):
    # Fetch the genres of the selected movie
    db_cursor.execute("SELECT genres FROM movie_data WHERE movie_title = %s", (selected_movie,))
    selected_movie_genres = db_cursor.fetchone()[0]

    # Query the database to retrieve movies with the same genre(s)
    db_cursor.execute("SELECT movie_title, movie_imdb_link FROM movie_data WHERE genres LIKE %s", ('%'+selected_movie_genres+'%',))
    similar_movies = db_cursor.fetchall()

    return similar_movies


def genres_based_recommendation(genres, imdb_score_min, imdb_score_max, n):
    # Construct SQL query to fetch movies based on selected genres and IMDb score range
    query = "SELECT movie_title, movie_imdb_link FROM movie_data WHERE "
    genre_conditions = " OR ".join([f"genres LIKE '%{genre}%'" for genre in genres])
    score_condition = f"imdb_score BETWEEN {imdb_score_min} AND {imdb_score_max}"
    query += f"({genre_conditions}) AND {score_condition} ORDER BY imdb_score DESC LIMIT {n}"
    
    # Execute the SQL query
    db_cursor.execute(query)
    recommended_movies = db_cursor.fetchall()
    
    # Return the list of recommended movies
    return recommended_movies




if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    db_cursor.execute("SELECT movie_title FROM movie_data")
    movie_titles = db_cursor.fetchall()
    movies = [title[0] for title in movie_titles]
    
    with st.container():
     left_column, right_column = st.columns(2)
     with left_column:
            st.write("")
            st.title('MOVIE RECOMMENDER ENGINE') 
     with right_column:
            st_lottie(lottie_coding, height=300,width=400, key="coding")
        
    

    apps = ['*--Select--*', 'Movie based', 'Genres based']   
    app_options = st.selectbox('Method Of Recommendation:', apps)


    
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select a movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select a movie')
        else:
            review_input = st.text_area("Write your review:")
            if st.button("Get Recommendations"):

                n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
                scores = sid.polarity_scores(review_input)
                if scores['compound'] > 0:
                    sentiment_label = "Positive"
                elif scores['compound'] < 0:
                    sentiment_label = "Negative"
                else:
                    sentiment_label = "Neutral"
                
                sql_update = "UPDATE movie_data SET label = %s WHERE movie_title = %s"
                db_cursor.execute(sql_update, (sentiment_label, movie_select))
                db_connection.commit()    
                
                # Fetch movie genres from the database
                similar_movies = get_similar_movies(movie_select)
                
                    
                
                
                st.write("")
                st.write("")
                st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> RECOMMENDED MOVIES 📈 </h1>", unsafe_allow_html=True)
                st.write("")
                st.write("")
            
                for movie, link in similar_movies:
                    st.warning(movie)
                    st.markdown(f"📌 IMDB LINK --- [{movie}]({link})")

        
    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score_min = st.slider('Min IMDb score:', 1, 10, 8)
            imdb_score_max = st.slider('Max IMDb score:', imdb_score_min, 10, 10)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            
            similar_movies = genres_based_recommendation(options, imdb_score_min,imdb_score_max, n)
            
            st.write("")
            st.write("")
            st. markdown("<h1 style='text-align: center; color:#A0CFD3;'> RECOMMENDED MOVIES 📈 </h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            
            if similar_movies:
                for movie, link in similar_movies:
                    st.warning(movie)
                    st.markdown(f"📌 IMDB LINK --- [{movie}]({link})")
                

        else:
                st.write(" _Can Select Multiple Genres_ ")
                        

    else:
        st.write('Select option')



        

st.write("---")
st. markdown("<h1 style='text-align:center; color:#A0CFD3;font-size:55px;font-family:monospace;float:right;'>EXPLORE THE CONTENT😏</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
components.iframe("https://docs.google.com/presentation/d/1rUnS1ooWiM92rk53oltDOLH1IB3b1om6vhguPntfH00/embed?start=true&amp;loop=true&amp;delayms=3000&amp;slide=id.gdfb5b8cfff_1_729&amp;usp=embed_facebook&slide=id.p2",width=670, height=400, scrolling=True)




st_lottie(lottie_loadLine,height=300,width=700,key="coding3")
st. markdown("<h1 style='text-align:center; color:#A0CFD3;font-size:60px;font-family:monospace;'> WANT TO CONNECT 👨‍⚖️</h1>", unsafe_allow_html=True)


st.write("")
with st.container():
    contact_form = """
    <form action="https://formsubmit.co/devansh131202@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" style="height:50px; width:300px; font-size:14pt; margin:5px;padding:10px;border-radius:5px;" placeholder="Your name" required>
        <input type="email" name="email" style="height:50px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your email" required>
        <textarea name="message" style="height:150px; width:300px; font-size:14pt;margin:5px;padding:10px;border-radius:5px;" placeholder="Your message here" required></textarea>
        <button style=" height:50px; width:300px; font-size:14pt; margin:5px; padding:10px;border-radius:5px;background-color:#90EE90" type="submit">Send</button>
        <input type="hidden" name="_next" value="https://github.com/DevanshVCodes/FormSubmit">
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

        
    with right_column:
        st_lottie(lottie_contact,height=300,width=400,key="coding2")



       