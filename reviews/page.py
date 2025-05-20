import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def reviews_page():

    reviews_service = ReviewService()
    reviews = reviews_service.get_reviews()

    st.title("Reviews")
    st.write("Welcome to the Reviews page!")
    
    if reviews:
        reviews_df = pd.json_normalize(reviews)
        AgGrid(data=reviews_df, 
            key="reviews_table",
            height=300,
            fit_columns_on_grid_load=True,
            )
    else:
        st.warning("No reviews found.")
    
    # Add a button to add a new review
    st.title("Add new review")
    movie_service = MovieService()
    movies = movie_service.get_movies()

    movies_title = {movie['title']: movie['id'] for movie in movies}
    selected_movie = st.selectbox("Select a movie", list(movies_title.keys()))

    rate = st.number_input("Rating", min_value=0, max_value=5, step=1)
    comment = st.text_area("Comment")

    if st.button("Add Review"):
        new_review = reviews_service.create_review(
            movie=movies_title[selected_movie],
            rate=rate,
            comment=comment
        )
        if new_review:
            st.success("Review added successfully!")
            st.rerun()
        else:
            st.error("Failed to add review.")