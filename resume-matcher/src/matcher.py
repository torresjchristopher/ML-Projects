from sentence_transformers.util import cos_sim

def compute_similarity(resume_embedding, jd_embedding):
    return cos_sim(resume_embedding, jd_embedding).item()
