import requests


class Auth:

    def __init__(self):
        self.__base_url = "https://joasjonson.pythonanywhere.com/api/v1/"
        self.__auth_url = f"{self.__base_url}auth/token/"

    def get_token(self, username, password):
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(self.__auth_url, 
                                 data=data)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Invalid credentials. Status code: {response.status_code}"}
