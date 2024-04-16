import streamlit as st
import os
from PIL import Image

st.markdown(
    """
    # ResumeRight (using ResuLLme)
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Visit-blue)](https://www.linkedin.com/in/bhavyachawla/)
    [![GitHub](https://img.shields.io/badge/GitHub-Visit-blue)](https://github.com/BhavyaChawlaGit)
    
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
### Table of Contents

- [Simple](#simple)
- [Awesome](#awesome)
- [BGJC](#bgjc)
- [Deedy](#deedy)
- [Modern](#modern)
- [Plush](#plush)
- [Alta](#alta)
"""
)

st.markdown(
    """
    ## Simple

    The most straightforward template, it also is the one that condenses the most information in a single page.
    This is the default for ResumeRight due to its reliability.
    """
)

current_dir = os.path.dirname(os.path.realpath(__file__))

simple_image = Image.open(f"{current_dir}/../../.github/images/Simple_Template.png")

st.image(simple_image)

st.markdown(
    """
    ## Awesome

    This is a popular template with nice fonts and design. It also condenses a lot of information in a single
    page. This is another strong candidate for the default template.
    """
)

awesome_image = Image.open(f"{current_dir}/../../.github/images/Awesome_Template.png")

st.image(awesome_image)

st.markdown(
    """
    ## BGJC

    Another classic, single-column template. It presents less information with clear separations among the sections.
    """
)

bgjc_image = Image.open(f"{current_dir}/../../.github/images/BGJC.png")

st.image(bgjc_image)

st.markdown(
    """
    ## Deedy

    This is a sleek two-column template. The template is more crowded, but it excells at using
    all the space available in the page.
    """
)

deedy_image = Image.open(f"{current_dir}/../../.github/images/Deedy.png")

st.image(deedy_image)

st.markdown(
    """
    ## Modern

    This is another take on the classic, single-column CV style. For a black-and-white template,
    it is an excellent choice.
    """
)

modern_image = Image.open(f"{current_dir}/../../.github/images/Modern.png")

st.image(modern_image)

st.markdown(
    """
    ## Plush

    This is a variant of the Deedy template with a stylish look. The order of the columns are swapped
    and the font is slightly different, giving it a distinct feeling from the other templates.
    """
)

plush_image = Image.open(f"{current_dir}/../../.github/images/Plush.png")

st.image(plush_image)

st.markdown(
    """
    ## Alta

    This is eye-candy template is another popular option. It speaks for itself.
    """
)

alta_image = Image.open(f"{current_dir}/../../.github/images/Alta_Template.png")

st.image(alta_image)
