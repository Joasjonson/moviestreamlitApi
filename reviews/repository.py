import requests
from login.service import logout
import streamlit as st


class ReviewRepository:

    def __init__(self):
        self.base_url = "https://joasjonson.pythonanywhere.com/api/v1/"
        self.reviews_url = f"{self.base_url}reviews/"
        self.headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

    def get_reviews(self):
        response = requests.get(self.reviews_url, headers=self.headers)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 401:
            st.error("Unauthorized. Please login again.")
            logout()

        else:
            st.error(f"Error: {response.status_code}")
            return None
        
    def create_review(self, review):
        response = requests.post(self.reviews_url, 
                                 headers=self.headers, 
                                 json=review)

        if response.status_code == 201:
            st.success("Review created successfully!")
            return response.json()

        elif response.status_code == 401:
            st.error("Unauthorized. Please login again.")
            logout()

        else:
            st.error(f"Error: {response.status_code}")
            return None