import streamlit as st

st.markdown(
    """
    # ResumeRight
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Visit-blue)](https://www.linkedin.com/in/bhavyachawla/)
    [![GitHub](https://img.shields.io/badge/GitHub-Visit-blue)](https://github.com/BhavyaChawlaGit)
    
    """,
    unsafe_allow_html=True,
)



# with st.expander("**Do I need an OpenAI API Key to run ResumeRight?**"):
#     st.markdown("""   
#     **No**, We provide all the support needed and can use our services freely.
#     """
#     )



# with st.expander("**Can I store my OpenAI API Key instead of manually re-entering it?**"):
#     st.markdown(
#     """
#     **No**, you cannot store your key, but in future if supported, ResumeRight will prompt the user for a key.
#     """
#     )

with st.expander("**I want to use my own custom format to render my résumé. Is this possible?**"):
    st.markdown(
    """
    Currently, you **cannot** use your own custom format for your résumé.
    """
    )

with st.expander("**What is the LaTeX format?**"):
    st.markdown(
    """
    LaTeX is a document preperation system that is used to render PDFs. ResumeRight uses LaTeX to render a new AI-curated résumé in a format chosen by you!
    """
    )


with st.expander("**What is the JSON schema for the résumé?**"):
    st.markdown(
    """
    To render the LaTeX file, we use a JSON schema to format data and allow standardized processing.
    """
    )
    

with st.expander("**There is information on my résumé that is not accurate. How do I fix it?**"):
    st.markdown(
    """
    Sometimes, LLMs can hallucinate and produce information that is not correct. If this happened to your résumé,
    there are two options to editing it:
        
    * Download the JSON file, and manually edit it using a text editor and render it again by going to [Render JSON Resume](/Render_JSON_Resume).
        
    * Download the LaTeX file and edit it on [Overleaf (or your favorite LaTeX editor)](/Edit_LaTeX_on_Overleaf).    

    """
    )
