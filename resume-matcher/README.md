# Resume Matcher

A semantic search tool to match resumes with job descriptions using NLP embeddings.

## Features

- Extracts text from PDF/DOCX resumes
- Embeds text using `sentence-transformers`
- Matches with job descriptions using cosine similarity
- Optional Streamlit UI

## Folder Structure

resume_matcher/
├── data/
│ ├── resumes/
│ └── job_descriptions/
├── src/
├── main.py
├── app.py
├── requirements.txt
└── README.md


## Setup Instructions

1. Install dependencies:

bash
pip install -r requirements.txt


2. Run the matcher script:

python main.py


3. Launch the Streamlit app:

streamlit run app.py
