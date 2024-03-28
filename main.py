import streamlit as st
from base import base
from about import about

import streamlit as st
import pandas as pd
from urllib.request import urlopen
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie
import streamlit_authenticator as sa

from active_list import active_list
from year_forecast import year_forecast
from accum_dep import accum_dep
from active_base import active_base

import pickle
from pathlib import Path 
import streamlit_authenticator as stauth 

from st_login_form import login_form

#Layout
st.set_page_config(
    page_title="Zenkos Investments (Pty) Ltd",
    layout="wide",
    initial_sidebar_state="expanded")

names = ["kossi toulassi","mr user"]
usernames = ["ktoulassi","testname"]

#Data Pull and Functions
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

# def main():

#Options Menu
with st.sidebar:
    # st.sidebar.title(f"Welcome {name}")
    client = login_form()
    selected = option_menu('Zenkos', ["Intro",
    'Active Listening Diagnostic',
    '12 Month Forecast',
    'Accumulated Depreciation',
    'Activity Based Costing',
    'About'], 
    icons=['play-btn','search','info-circle'],menu_icon='intersect', default_index=0)
    # authenticator.logout("Logout","sidebar")
    lottie = load_lottiefile("similo3.json")
    st_lottie(lottie,key='loc')    

if st.session_state['authenticated']:    

    if selected == "Intro":    
        base()
    elif selected == "Active Listening Diagnostic":
        active_list()
    elif selected == "12 Month Forecast":
        year_forecast()
    elif selected == "Accumulated Depreciation":
        accum_dep()
    elif selected == "Activity Based Costing":
        active_base()
    elif selected == "About":
        about()

# if __name__ == "__main__":
#     main()
