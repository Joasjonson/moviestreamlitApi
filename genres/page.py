import streamlit as st
import pandas as pd
from genres.service import GenreService
from st_aggrid import AgGrid


def genres_page():

    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.title("Genres")
        st.write("Welcome to the Genres page!")
        
        st.write("This is where you can explore different genres of movies.")
        genres_df = pd.json_normalize(genres)
        AgGrid(data=genres_df, 
            reload_data=True,
            key="genres_table",
            height=350,
            fit_columns_on_grid_load=True,
            )
    else:
        st.warning("Failed to load genres. Please try again later.")


    # Add a button to add a new genre
    st.title("Add a new genre")
    new_genre = st.text_input("Enter the name of the new genre")
    if st.button("Add Genre"):
        if new_genre:
            genre_service.create_genre(new_genre)
            st.success(f"Genre '{new_genre}' added successfully!")
            st.rerun()
        else:
            st.error("Please enter a genre name.")
