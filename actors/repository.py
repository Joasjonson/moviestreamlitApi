import requests
import streamlit as st
from login.service import logout


class ActorRepository:

    def __init__(self):
        self.base_url = "https://joasjonson.pythonanywhere.com/api/v1/"
        self.actors_url = f"{self.base_url}actors/"
        self.headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_actors(self):
        response = requests.get(self.actors_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch actors.")
            return None
        

    def create_actor(self, new_actor):
        response = requests.post(self.actors_url, headers=self.headers, data=new_actor)

        if response.status_code == 201:
            st.success("Actor added successfully!")
            return response.json()
        
        elif response.status_code == 401:
            st.error("Unauthorized. Please login again.")
            logout()
        else:
            st.error("Failed to add actor.")
            return None