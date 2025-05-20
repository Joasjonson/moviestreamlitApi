import streamlit as st
from genres.page import genres_page
from actors.page import actors_page
from movies.page import movies_page
from reviews.page import reviews_page
from login.page import login_page
from home.page import show_home

def main():
    st.title("Flix App - Streamlit")

    if "token" not in st.session_state:
        login_page()

    else:

        option_menu = st.sidebar.selectbox("Select an option", ["Home", "Movies", "Genres", "Actors", "Reviews"])

        if option_menu == "Home":
            show_home()

        elif option_menu == "Movies":
            movies_page()
        
        elif option_menu == "Genres":
            genres_page()

        elif option_menu == "Actors":
            actors_page()

        elif option_menu == "Reviews":
            reviews_page()

    
    
    
    

if __name__ == "__main__":
    main()

