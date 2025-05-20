import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from actors.service import ActorService
import datetime


def actors_page():

    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.title("Actors")
        st.write("List of Actors")
        
        actors_df = pd.json_normalize(actors)
        AgGrid(data=actors_df, 
            key="actors_table",
            height=350,
            fit_columns_on_grid_load=True,
            )
    else:
        st.warning("Failed to load actors. Please try again later.")


    # Add a button to add a new actor
    st.title("Add a new actor")
    name_actor = st.text_input("Name of the actor:")
    birthday_actor = st.date_input(label="Enter the birthday of the actor:",
                                   value=datetime.date.today(),
                                   min_value=datetime.date(1900, 1, 1),
                                   max_value=datetime.date.today(),
                                   format="YYYY-MM-DD",
                                   help="Enter the birthday of the actor in YYYY-MM-DD format")
    
    nationality_choices = [
    'US', 'CA', 'MX', 'GB', 'FR', 'DE', 'IT', 'JP', 'KR', 'CN',
    'IN', 'BR', 'AU', 'ES', 'RU', 'ZA', 'NG', 'AR', 'NL', 'SE',
    'CH', 'BE', 'IE', 'PT']

    nationality_actor = st.selectbox("Select the nationality of the actor:", nationality_choices)

    if st.button("Add Actor"):
        if name_actor and birthday_actor and nationality_actor:
            actor_service.create_actor(name_actor, 
                                       birthday_actor.strftime("%Y-%m-%d"), 
                                       nationality_actor)
            
            st.success(f"Actor '{name_actor}' added successfully!")
            st.rerun()
        else:
            st.error("Please enter all fields.")
    

