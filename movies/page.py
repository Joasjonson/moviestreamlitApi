import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService
import datetime


def movies_page():

    movie_service = MovieService()
    movies = movie_service.get_movies()

    st.title("Movies")
    st.write("Welcome to the Movies page!")
    
    if movies:
        movies_df =  pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=["actors", "genre.id"])

        AgGrid(data=movies_df,             
            key="movies_table",
            height=300,            
            )
    else:
        st.error("No movies found.")
    
    # Add a button to add a new movie
    st.title("Add new movie")
    
    title = st.text_input("Title")
    release_date = st.date_input(label="Enter the release date of the movie:",
                                 value=datetime.date.today(),
                                 min_value=datetime.date(1900, 1, 1),
                                 max_value=datetime.date.today(),
                                 format="YYYY-MM-DD",
                                 help="Enter the release date of the movie in YYYY-MM-DD format")
                                 
    # Get genres from GenreService
    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}
    genre = st.selectbox("Select the genre of the movie:", list(genre_names.keys()))

    # Get id of actors from ActorService
    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = { actor['name']: actor['id'] for actor in actors}
    actor_names_selected = st.multiselect("Select the actors of the movie:", list(actor_names.keys()))
    actors_ids = [actor_names[actor] for actor in actor_names_selected]

    resume = st.text_area("Resume")

    if st.button("Add Movie"):
        new_movie = movie_service.create_movie(
            title=title,
            genre=genre_names[genre],
            release_date=release_date,
            actors=actors_ids,
            resume=resume
        )
        if new_movie:        
            st.success(f"Movie {title} added successfully!") 
            st.balloons()
            st.rerun()      
    else:
        st.warning("Please fill in all fields.")       
