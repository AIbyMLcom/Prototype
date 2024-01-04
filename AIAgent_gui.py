# -*- coding: utf-8 -*-
"""
  Copyright 2022 

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

import streamlit as st
from PIL import Image

from util.functions.path import get_file_path, get_dir_name, util_str, data_str
from util.pages.home_page import home_page
from util.pages.overview_page import overview_page
#from agent import officeassistant_page
#from util.pages import researchassistant_page
#from util.pages import teachingassistant_page
#from util.pages import managerassistant_page
#from util.pages import professionalassistant_page
img = Image.open(
        get_file_path(
            "aibyml_logo.ico",
            dir_path=f"{get_dir_name(__file__)}/{util_str}/{data_str}",
            )
        )
        
st.set_page_config(page_title="AIAgent", page_icon=img, layout="wide")


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):

        st.sidebar.markdown("## AI Assitant")

        app = st.sidebar.selectbox(
            "Select Your Type of AI", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()


app = MultiApp()

app.add_app("Home Page", home_page)
app.add_app("Service Overview", overview_page)
#app.add_app("AI Office Assistant", officeassistant_page)
#app.add_app("AI Research Assistant", researchassistant_page)
#app.add_app("AI Teaching Assistant", teachingassistant_page)
#app.add_app("AI Manager Assistant", managerassistant_page)
#app.add_app("Professional Assistant", professionalassistant_page)


app.run()
