import streamlit as st
import streamlit_ext as ste
import os
import openai



from doc_utils import extract_text_from_upload
from templates import generate_latex, template_commands
from prompt_engineering import generate_json_resume, tailor_resume
from render import render_latex
import json

if __name__ == '__main__':
    
    st.set_page_config(
        page_title="ResumeRight",
        page_icon=":clipboard:",
        layout="wide",
        initial_sidebar_state="auto",
    )
    
    IFRAME = '<iframe src="https://ghbtns.com/github-btn.html?user=IvanIsCoding&repo=ResuLLMe&type=star&count=true&size=large" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>'


    st.markdown(
        f"""
        # ResumeRight (using ResuLLme) {IFRAME}
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-Visit-blue)](https://www.linkedin.com/in/bhavyachawla/)
        [![GitHub](https://img.shields.io/badge/GitHub-Visit-blue)](https://github.com/BhavyaChawlaGit)
        
        """,
        unsafe_allow_html=True,
    )


    uploaded_file = st.file_uploader("Drop your Resume here", type=["pdf", "docx", "txt", "json"])

    template_options = list(template_commands.keys())

    if uploaded_file is not None:
        # Get the CV data that we need to convert to json
        text = extract_text_from_upload(uploaded_file)

        # If the OpenAI API Key is not set as an environment variable, prompt the user for it
        # openai_api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = "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"

        # if not openai_api_key:
        #     openai_api_key = st.text_input(
        #         "Enter your OpenAI API Key: [(click here to obtain a new key if you do not have one)](https://platform.openai.com/account/api-keys)",
        #         type="password",
        #     )

        chosen_option = st.selectbox(
            "Select a template to use for your resume [(see templates)](/Template_Gallery)",
            template_options,
            index=0,  # default to the first option
        )

        section_ordering = st.multiselect(
            "Optional: which section ordering would you like to use?",
            ["education", "work", "skills", "projects", "awards"],
            ["education", "work", "skills", "projects", "awards"],
        )

        improve_check = st.checkbox("I want to improve the resume with LLMs", value=True)

        generate_button = st.button("Generate Resume")

        if generate_button:
            try:
                if improve_check:
                    with st.spinner("Tailoring the resume"):
                        text = tailor_resume(text, openai.api_key)

                json_resume = generate_json_resume(text, openai.api_key)
                latex_resume = generate_latex(chosen_option, json_resume, section_ordering)

                resume_bytes = render_latex(template_commands[chosen_option], latex_resume)

                col1, col2, col3 = st.columns(3)

                try:
                    with col1:
                        btn = ste.download_button(
                            label="Download PDF",
                            data=resume_bytes,
                            file_name="resume.pdf",
                            mime="application/pdf",
                        )
                except Exception as e:
                    st.write(e)

                with col2:
                    ste.download_button(
                        label="Download LaTeX Source",
                        data=latex_resume,
                        file_name="resume.tex",
                        mime="application/x-tex",
                    )

                with col3:
                    ste.download_button(
                        label="Download JSON Source",
                        data=json.dumps(json_resume, indent=4),
                        file_name="resume.json",
                        mime="text/json",
                    )
            # except openai.RateLimitError as e:
            #     st.markdown(
            #         "It looks like you do not have OpenAI API credits left. Check [OpenAI's usage webpage for more information](https://platform.openai.com/account/usage)"
            #     )
                # st.write(e)
            except Exception as e:
                st.error("An error occurred while generating the resume. Please try again.")
                st.write(e)
    else:
        st.info("Please upload atleaset a file to get started.")



with st.expander("**There is information on my résumé that is not accurate. How do I fix it?**"):
    st.markdown(
    """
    Sometimes, LLMs can hallucinate and produce information that is not correct. If this happened to your résumé,
    there are two options to editing it:
        
    * Download the JSON file, and manually edit it using a text editor and render it again by going to [Render JSON Resume](/Render_JSON_Resume).
        
    * Download the LaTeX file and edit it on [Overleaf (or your favorite LaTeX editor)](/Edit_LaTeX_on_Overleaf).    

    """
    )