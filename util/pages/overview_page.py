# -*- coding: utf-8 -*-
"""
  Copyright 2022 Mitchell Isaac Parker

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

import streamlit as st
from PIL import Image

from ..functions.table import mask_equal
from ..functions.col import pdb_code_col
from ..functions.path import pages_str, data_str, get_file_path
from ..functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path

def overview_page():

    st.markdown("# Service Overview")
    
    st.markdown("---")
        
    st.markdown("## Introduction to the AI Assistant")
    
    left_col, right_col = st.columns(2)
    
    with left_col: 
        st.markdown("#### An Artificial Intelligence Assistant (AIA) is an agent acting in a cognitive manner;")
        st.markdown("#### It perceives its environment or instructions, takes actions autonomously in order to achieve goals, and may able to improve its performance with learning or acquiring knowledge.")

    with right_col:
        video_file = open('TalkingPhoto.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    st.sidebar.markdown(
        "**Note.** See the Definition [*Wikipedia*](https://en.wikipedia.org/wiki/Intelligent_agent)."
    )
    
    img = Image.open(
        get_file_path(
            "AI-Agent-Workflow.png",
            dir_path=get_neighbor_path(__file__, pages_str, data_str),
        )
    )

    st.image(img, output_format="PNG")
    st.markdown("#### An intelligent agent may be complex as a human worker, as is any working environment that meets the job requirements, the objective and the task.")


    officeassistant_task_dict = {
        "Reception": "https://github.com/shreyabhadwal/AI-Receptionist",
        "Sort Document": "https://huggingface.co/spaces/Wootang01/document_classifier/tree/main",
        "Sending email": "https://medium.com/llm-projects/llm-app-tutorial-building-your-own-auto-email-follow-up-10006c39e860",
        "Arrange Activities": "https://www.youtube.com/watch?v=0BwY9IiZ6h8",
        "Email Marketing": "https://www.sendlane.com/blog/chat-gpt-and-email-marketing",
        "Help Recruit": "https://github.com/AIBIZSERVICE/CVReader"
    }

    st.sidebar.markdown("## Office Task GPT Links")
    
    link_1_col, link_2_col= st.sidebar.columns(2)

    i = 0
    link_col_dict = {0: link_1_col, 1: link_2_col}
    
    for link_text, link_url in officeassistant_task_dict.items():

        st_col = link_col_dict[i]
        i += 1
        if i == len(link_col_dict.keys()):
            i = 0

        create_st_button(link_text, link_url, st_col=st_col)

    researchassistant_task_dict = {
        "Data Visual": "https://pypi.org/project/pandas-profiling/",
        "Document Search": "https://github.com/aju22/DocumentGPT",
        "Summary Paper": "https://huggingface.co/spaces/aibyml/SummarizeDoc",
        "Book Report": "https://huggingface.co/spaces/cklbckoho/NTBkReport",
        "Data Analytics": "https://huggingface.co/spaces/aibyml/PeopleAnalytics",
        "Classification": "https://github.com/AIBIZSERVICE/Classification",
        "Regression": "https://github.com/AIBIZSERVICE/Regression",
        "Textual Analysis": "https://github.com/AIBIZSERVICE/TextualAnalysis",
        "Clustering": "https://github.com/AIBIZSERVICE/Clustering"
    }

    st.sidebar.markdown("## Reseach Tool Links")
    
    link_1_col, link_2_col= st.sidebar.columns(2)

    i = 0
    link_col_dict = {0: link_1_col, 1: link_2_col}
    
    for link_text, link_url in researchassistant_task_dict.items():

        st_col = link_col_dict[i]
        i += 1
        if i == len(link_col_dict.keys()):
            i = 0

        create_st_button(link_text, link_url, st_col=st_col)

    teachingassistant_task_dict = {
        "Draft Outline": "https://www.youtube.com/watch?v=_z6Ute4wprs",
        "Tutorial": "https://medium.com/@lampmaa22/free-llm-gpt-tutorial-from-esther-7cc6b49d147e",
        "Talk to Student": "https://github.com/daveshap/TutorChatbot",
        "Set Questions": "https://github.com/AIBIZSERVICE/SetQuestions",
        "Marking Essay": "https://github.com/AIBIZSERVICE/MarkingEssay",
        "Manage Activity": "https://github.com/AIBIZSERVICE/ManageActivity",
    }

    st.sidebar.markdown("## Teaching Agent GPT Links")
    
    link_1_col, link_2_col= st.sidebar.columns(2)

    i = 0
    link_col_dict = {0: link_1_col, 1: link_2_col}
    
    for link_text, link_url in teachingassistant_task_dict.items():

        st_col = link_col_dict[i]
        i += 1
        if i == len(link_col_dict.keys()):
            i = 0

        create_st_button(link_text, link_url, st_col=st_col)

    st.markdown("---")

    st.markdown("## Our Mechanism")
    st.markdown("---")
    img = Image.open(
        get_file_path(
            "AI-Agent-Serviceflow.png",
            dir_path=get_neighbor_path(__file__, pages_str, data_str),
        )
    )

    st.image(img, output_format="PNG")
    

    st.markdown('## Types of AI Assistant')
    st.markdown('### Pages on Type AI Assistants:')
    st.markdown('#### (*left column*, a menu for navigating to)')
    
    st.markdown("---")
    
    st.markdown('## Difference Between ChatGPT and Our Services')
    
    st.markdown('### *You can own your GPT or AI.')
    st.markdown('### *You do not need to share data with Apps Providers')
    st.markdown('### *You have cybersecurity protection by Cloud Service Provider (AWS, AZURE or etc)')
    st.markdown('#### - Through your insights and feedback, fine-tune the GPT is *YOUR ASSET*, ensured by NFT and blockchain')
    st.markdown('#### - If you need, we can build *YOUR FOUNDATION GPT*, like ChatGPT3.5, in a machine belong to YOU, less than HK$5000')
        
    
    st.markdown("---")

    left_info_col, right_info_col = st.columns(2)

    left_info_col.markdown(
        f"""
        ### contact
        Please feel free to contact us with any issues, comments, or questions.

        ##### Victor Hung [![Linkedin URL]()

        - Email:  <@admin@aibyml.com> or <rhythm.victorius@me.com>
        - GitHub: https://github.com/AIBIZSERVICE

        """,
        unsafe_allow_html=True,
    )

    right_info_col.markdown(
        """
        ### License
        Apache License 2.0
        """
    )

    write_st_end()

