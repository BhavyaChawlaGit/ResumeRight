#from dotenv import load_dotenv
import os
import base64
import streamlit as st
import io
import pdfplumber
import openai
import docx
import psycopg2



# Replace 'your-api-key' with your actual API key
#openai.api_key = "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"
openai.api_key = st.secrets["OPENAI_API_KEY"]



def get_gpt3_response(input, pdf_content, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a smart assistant to career advisors at the Harvard Extension School. Your take is to write Cover letters to be more brief and convincing according to the Resumes and Cover Letters guide."}, 
            {"role": "user", "content": f"{input} {pdf_content} {prompt}"},
        ],
    )
    return response['choices'][0]['message']['content']

    #  You are an advanced AI acting as a virtual consultant for job applicants. Your task is to analyze resumes and job descriptions to provide a detailed compatibility assessment. This assessment should be structured as a professional narrative that smoothly transitions between the applicants strengths, areas for improvement, and tailored recommendations. Your output must adhere to high standards of clarity and professionalism, mirroring the quality expected in top-tier consultancy reports.
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         # Convert the PDF to text
#         with pdfplumber.open(uploaded_file) as pdf:
#             first_page = pdf.pages[0]
#             text = first_page.extract_text()

    # pdf_bytes = uploaded_file.read()
    # # Use pdfplumber with a file-like object created from pdf_bytes
    # with pdfplumber.PDF(io.BytesIO(pdf_bytes)) as pdf:
    #     first_page = pdf.pages[0]
    #     text = first_page.extract_text()
    # return text

# Provisioned to be used with pdfplumber==0.11.2, currently we are on pdfplumber==0.11.0

def input_pdf_setup(uploaded_file):
    pdf_bytes = uploaded_file.read()
    try:
        # Use pdfplumber with a file-like object created from pdf_bytes
        with pdfplumber.PDF(io.BytesIO(pdf_bytes)) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text()
    except ValueError as e:
        print(f"Encountered an error while extracting text: {e}")
        text = None  # Handle the error as appropriate for your application
#     return text

st.set_page_config(
        page_title="ResumeRight",
        # page_icon=":document:",
        layout="wide",
        initial_sidebar_state="auto",
    )


st.markdown(
    """
    # ResumeRight
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-Visit-blue)](https://www.linkedin.com/in/bhavyachawla/)
    [![GitHub](https://img.shields.io/badge/GitHub-Visit-blue)](https://github.com/BhavyaChawlaGit)
    
    """,
    unsafe_allow_html=True,
)

st.markdown(
        "Welcome to ResumeRight! Drop JobDescription and your Resume below, and let us analyze it for you"
    )


input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    pdf_content = input_pdf_setup(uploaded_file)
else:
    pdf_content = None
    


submit1 = st.button("Evaluate My Job Fit")
# submit2 = st.button("How Can I Improvise my Resume")
submit2 = st.button("Percentage Match")
submit3 = st.button("Cover Letter")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """



input_prompt1 = """
You are an advanced AI trained to provide detailed and professional job fit analyses. Evaluate the provided resume against the specified job description, crafting a coherent narrative for the candidate that highlights how the candidate’s background aligns with the job requirements.
Ensure that the output flows logically from one section to the next, maintaining a narrative that seamlessly connects the evaluation points into a single paragraph, and reflects a professional tone suitable for high-level career assessments.

Your analysis should be structured as follows:
1. Introduction: Start by summarizing the candidate’s key qualifications and experiences that are directly relevant to the job.
2. Strengths and Compatibility: Discuss the candidate’s strongest qualifications and how these strengths specifically meet the job’s demands. Use examples from the resume to illustrate these points and subtly begin to introduce areas where these strengths can compensate for any weaknesses.
3. Areas Needing Improvement: Smoothly transition from strengths to areas needing improvement by contrasting them. Explain what qualifications, skills, or certifications are missing, and why these are critical for the job.
4. Actionable Recommendations: Offer specific and practical steps the candidate can take to acquire the missing qualifications or gain the necessary experience. Link these recommendations back to the candidate’s existing strengths, suggesting how they can leverage their current skills to master new areas quickly.
5. Conclusion: Conclude with an overall assessment of the candidate's fit for the position, summarizing how the recommended actions will enhance their suitability and readiness for the role.

"""






# input_prompt2 = """
# You are an experienced Human Resource Manager, your task is to review the provided resume against the job description.
# Please provide feedback on how the candidate can improve their resume to better align with the job requirements.
# In the ouput highlight the areas that need improvement and suggest changes or an updated resume to enhance the candidate's profile per the job description.
# Do not add any information which is not present in the resume, Also make a verification check whether the attached data is 
# """


input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing in bullet points and last final thoughts. 
Please make sure the output is clear and concise for the applicant to understand.
"""

# input_prompt3 = """
# You are a smart assistant to career advisors at the Harvard Extension School. Your take is to write a cover letter to be more brief and convincing according to the Resumes and Cover Letters guide. your task is to review and write a CV against the given Resume and job description.
# It should be 300-500 words long. Do not include dates or addresses in the cover letter. and follow below guidelines.

# Your task is to write the CV. Follow these guidelines:
# - Be truthful and objective to the experience listed in the CV
# - Be specific rather than general
# - write job highlight items using STAR methodology (but do not mention STAR explicitly)
# - Fix spelling and grammar errors
# - Writte to express not impress
# - Articulate and don't be flowery
# - Prefer active voice over passive voice
# - Do not include a summary about the candidate

# """

input_prompt3 = """
You are a smart assistant to career advisors at the Harvard Extension School. Your task is to write a concise and compelling cover letter based on the provided resume and job description. The cover letter should be 300-500 words long, adhering to the guidelines of the Resumes and Cover Letters guide. 

Please follow these guidelines to ensure the cover letter is effective:
- Remain truthful and objective about the experience listed in the resume.
- Be specific in describing achievements; generalize only when necessary for cohesion.
- Articulate job highlights using the STAR methodology for describing achievements (Situation, Task, Action, Result), without explicitly mentioning "STAR."
- Ensure the language is clear and direct, using an active voice to convey achievements and qualifications.
- Avoid unnecessary flourishes; write to express the candidate’s qualifications succinctly.
- Do not include dates, addresses, or a summary introduction about the candidate.
- Review and correct any spelling and grammar errors to maintain professionalism.

This cover letter should introduce the candidate's relevant qualifications and directly relate them to the job requirements, demonstrating why the candidate is a suitable match for the position.
"""




if not input_text:
        st.error("Please enter job description/requirements.")
elif not pdf_content:
        st.error("Please upload a PDF.")
else:
    if submit1:
        response = get_gpt3_response(input_text, pdf_content, input_prompt1)
        st.text_area('Response:', response, height=500)
    elif submit2:
        response = get_gpt3_response(input_text, pdf_content, input_prompt2)
        st.text_area('Response:', response, height=500)
    # elif submit3:
    #     response = get_gpt3_response(input_text, pdf_content, input_prompt3)
    #     st.text_area('Response:', response, height=500)
    elif submit3:
        
        if submit3:

            
            response = get_gpt3_response(input_text, pdf_content, input_prompt3)
            doc = docx.Document()
            doc.add_paragraph(response)
            doc.save("CoverLetter.docx")
            
            st.success("Your cover letter is ready for download!")
            

            # Read the contents of the file
            with open("CoverLetter.docx", "rb") as file:
                file_data = file.read()

        
            # Create a download button for the file
            st.download_button(
                label="Download the generated cover letter",
                data=file_data,
                file_name="CoverLetter.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.text_area('Response:', response, height=500)



