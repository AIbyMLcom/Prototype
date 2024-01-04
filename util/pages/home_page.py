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

import streamlit as st
from PIL import Image

from ..functions.table import mask_equal
from ..functions.col import pdb_code_col
from ..functions.path import pages_str, data_str, get_file_path
from ..functions.gui import load_st_table, write_st_end, create_st_button, show_st_structure, get_neighbor_path

def home_page():

    left_col, right_col = st.columns(2)

#
    df = load_st_table(__file__)

    show_st_structure(mask_equal(df, pdb_code_col, "6zj0"),
            zoom=1.2,
            width=400,
            height=300,
            cartoon_trans=0,
            surface_trans=1,
            spin_on=True,
            st_col=left_col)
#

    left_col.markdown("6ZJ0 protein, belongs to a family of RAS (KRAS, NRAS, and HRAS). Scientists believe use it to make drugs to cure many cancers.")
    
    right_col.markdown("# AI Assistant Creation Services")
    right_col.markdown("## Our tools to CREATE Your AI assistant")
    right_col.markdown("### Up to your choice on kinds of AI YOU like to make")
    right_col.markdown("**served by Victor Hung and his Team**")
    right_col.markdown("**AIbyML.com**")

    database_link_dict = {
        "IMF Paper about AI on Economies": "https://www.imf.org/en/Publications/fandd/issues/2023/12/Macroeconomics-of-artificial-intelligence-Brynjolfsson-Unger",
        "Proxy Data Base": "https://www.aibyml.com/data",
    }
    
    st.sidebar.markdown("## Related Links")
    for link_text, link_url in database_link_dict.items():
        create_st_button(link_text, link_url, st_col=st.sidebar)

    community_link_dict = {
        "Deep Learning: AI Forum": "https://community.deeplearning.ai/",
        "LangChain Bloc": "https://blog.langchain.dev/",
        "Microsoft AutoGen Research": "https://www.microsoft.com/en-us/research/project/autogen/",
    }

    st.sidebar.markdown("## Community-Related Links")
    for link_text, link_url in community_link_dict.items():
        create_st_button(link_text, link_url, st_col=st.sidebar)

    software_link_dict = {
        "LangChain": "https://www.langchain.com/",
        "Matplotlib": "https://matplotlib.org",       
        "NumPy": "https://numpy.org",
        "OpenAI": "https://openai.com/", 
        "Pandas AI": "https://docs.pandas-ai.com/en/latest/",
        "RAG GPT": "https://github.com/Azure/GPT-RAG.git",
        "SciPy": "https://scipy.org",
        "Seaborn": "https://seaborn.pydata.org",
        "Sklearn": "https://scikit-learn.org/stable/",
        "Streamlit": "https://streamlit.io",
        "Transformer": "https://huggingface.co/",
    }

    st.sidebar.markdown("## Software-Related Links")
    
    link_1_col, link_2_col, link_3_col = st.sidebar.columns(3)

    i = 0
    link_col_dict = {0: link_1_col, 1: link_2_col, 2: link_3_col}
    
    for link_text, link_url in software_link_dict.items():

        st_col = link_col_dict[i]
        i += 1
        if i == len(link_col_dict.keys()):
            i = 0

        create_st_button(link_text, link_url, st_col=st_col)

    st.markdown("---")

    st.markdown("## Introduction")
    st.markdown("### Our tool like 6ZJ0 protein by making AI for anyone, could build a better society for all.")
    st.markdown("#### We believe our work change the path of AI to serfdom, “mechanical slaves,” in future as discussed in [*AI Research by Sikdelsky*](https://www.project-syndicate.org/commentary/automation-may-not-boost-worker-income-by-robert-skidelsky-2019-02).")
    st.markdown("###  We make Your AI to Serve or Work Together with Your Human Intelligence.")
    st.markdown("### Recognising working with AI now could make you better in future")
    st.markdown("## The AI Era is coming")
    
    st.markdown("---")
    
    left_col, right_col = st.columns(2)
    
    img = Image.open(
        get_file_path(
            "AIbyMLcom.png",
            dir_path=get_neighbor_path(__file__, pages_str, data_str),
        )
    )

    right_col.image(img, output_format="PNG")
    

    left_col.markdown('## What we offer')
    left_col.markdown('### Overview **left column** how our services help you make your AI Assistant')
    left_col.markdown('#### and')
    left_col.markdown('### Pages on different AI Assistants:')
    left_col.markdown('#### (*left column*, a menu for navigating to)')
    
    left_col.markdown('#### *AI Office Assistant:* Assist you to do the office work.')
    left_col.markdown('#### *AI Research Assistant:* Help you to do research.')
    left_col.markdown('#### *AI Teaching Assistant:* Facilitate your teaching.')
    left_col.markdown('##### *AI Manager Assistant:* Manage your business work (to be built).')
    left_col.markdown('##### *AI Professional Assistant:* Enhance the scale of your services (to be built).')
        
    
    st.markdown("---")

    left_info_col, right_info_col = st.columns(2)

    left_info_col.markdown(
        f"""
        ### Contact us
        Please feel free to contact us with any issues, comments, or questions.

        ##### Victor Hung [![Linkedin URL]()

        - Email:  <@admin@aibyml.com> or <rhythm.victorius@me.com>
        - GitHub: https://github.com/AIBIZSERVICE

        """,
        unsafe_allow_html=True,
    )

    right_info_col.markdown(
        """
        ### Funding

        - Depend on who has the vision to fund us
        - Apply to Science Park or Cyberport
         """
    )

    right_info_col.markdown(
        """
        ### License
        Apache License 2.0
        """
    )

    write_st_end()
