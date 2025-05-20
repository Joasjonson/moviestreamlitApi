import streamlit as st
from movies.service import MovieService
import plotly.express as px
import pandas as pd
from collections import Counter


def show_home():
    st.title("🎬 Welcome to the Flix App!")
    st.write("This is a simple application to manage movies, genres, actors, and reviews.")
    
    movie_service = MovieService()
    movies_stats = movie_service.get_movie_stats()
    movies = movie_service.get_movies()

    if not movies_stats:
        st.error("Failed to fetch movie statistics.")
        return

    st.title("📊 Movie Statistics")

    # Displaying movie statistics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(label="Total Movies", value=movies_stats["total_movies"])
    col2.metric(label="Unique Genres", value=movies_stats["movies_genres"])
    col3.metric(label="Total Reviews", value=movies_stats["total_reviwews"])
    col4.metric(label="Average Rating", value=movies_stats["avg_rate"])

    # Bars chart
    stats_data = pd.DataFrame({
        "Category": ["Movies", "Genres", "Reviews", "Average Rating"],
        "Count": [
            movies_stats["total_movies"],
            movies_stats["movies_genres"],
            movies_stats["total_reviwews"],
            movies_stats["avg_rate"]
        ]
    })

    fig = px.bar(stats_data, x="Count", y="Category", orientation='h',
                 title="Overview of Movie Stats", text_auto=True,
                 color="Category", color_discrete_sequence=px.colors.qualitative.Set2)

    st.plotly_chart(fig)

    st.subheader("🍕 Movies by Genre ")
    genres = [movie["genre"]["name"] for movie in movies if movie.get("genre")]
    genre_counts = Counter(genres)
    genre_df = pd.DataFrame(genre_counts.items(), columns=["Genre", "Count"])

    if not genre_df.empty:
        pie_fig = px.pie(
            genre_df,
            names="Genre",
            values="Count",
            title="Distribution of Movies by Genre",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(pie_fig)
    else:
        st.warning("No genre data available to display.")


    
    st.subheader("🎞️ Movies by Genre ")
    genres = [movie["genre"]["name"] for movie in movies if movie.get("genre")]
    genre_counts = Counter(genres)
    genre_df = pd.DataFrame(genre_counts.items(), columns=["Genre", "Count"])

    if not genre_df.empty:
        bar_fig = px.bar(
            genre_df,
            x="Genre",
            y="Count",
            title="Number of Movies per Genre",
            text_auto=True,
            color="Genre",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(bar_fig)
    else:
        st.warning("No genre data available to display.")
    
    