import requests
import streamlit as st
from login.service import logout


class MovieRepository:
    
    def __init__(self):
        self.base_url = "https://joasjonson.pythonanywhere.com/api/v1/"
        self.movies_url = f"{self.base_url}movies/"
        self.headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_movies(self):
        response = requests.get(self.movies_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 401:
            st.error("Session expired. Please log in again.")
            logout()
            return None
        else:
            st.error("Failed to fetch movies.")
            st.error(f"Error: {response.status_code}")
            return None
        
    
    def create_movie(self, movie):
        response = requests.post(self.movies_url, 
                                 headers=self.headers, 
                                 data=movie)

        if response.status_code == 201:
            return response.json()
        
        elif response.status_code == 401:
            st.error("Session expired. Please log in again.")
            logout()
            return None
        raise Exception(f"Failed to create movie. Error: {response.status_code}")
    
    
    def get_movie_stats(self):
        response = requests.get(f"{self.movies_url}stats/", headers=self.headers)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 401:
            st.error("Session expired. Please log in again.")
            logout()
            return None
        else:
            st.error("Failed to fetch movies stats.")
            st.error(f"Error: {response.status_code}")
            return None