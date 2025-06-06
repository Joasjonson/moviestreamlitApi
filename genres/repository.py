import streamlit as st
import requests
from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = "https://joasjonson.pythonanywhere.com/api/v1/"
        self.__genres_url = f"{self.__base_url}genres/"
        self.__headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_genres(self):
        response = requests.get(self.__genres_url, headers=self.__headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            st.error("Unauthorized. Please login again.")
            logout()    

        else:
            st.error(f"Error: {response.status_code}")
            return None
    

    def create_genre(self, genre):
        response = requests.post(self.__genres_url, headers=self.__headers, data=genre)
        
        if response.status_code == 201:
            st.success("Genre created successfully!")
            return response.json()
        
        elif response.status_code == 401:
            st.error("Unauthorized. Please login again.")
            logout()    

        else:
            st.error(f"Error: {response.status_code}")
            return None


