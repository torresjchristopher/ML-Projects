import os
from src.parser import extract_text_from_pdf, load_job_description
from src.embedder import embed_text
from src.matcher import compute_similarity

resumes_dir = 'data/resumes'
job_desc_path = 'data/job_descriptions/software_engineer.txt'

jd_text = load_job_description(job_desc_path)
jd_embedding = embed_text(jd_text)

results = []

for filename in os.listdir(resumes_dir):
    if filename.endswith('.pdf'):
        path = os.path.join(resumes_dir, filename)
        resume_text = extract_text_from_pdf(path)
        resume_embedding = embed_text(resume_text)
        score = compute_similarity(resume_embedding, jd_embedding)
        results.append((filename, score))

# Sort by similarity
results.sort(key=lambda x: x[1], reverse=True)

for name, score in results:
    print(f"{name}: {score:.4f}")
