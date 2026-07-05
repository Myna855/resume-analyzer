import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from data.skills import ALL_SKILLS

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _extract_keywords(text: str) -> list:
    lower = text.lower()
    found = []
    for skill in ALL_SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, lower):
            found.append(skill)
    return found


def match_job(resume_text: str, jd_text: str) -> dict:
    # TF-IDF cosine similarity
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    try:
        tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_score = int(round(similarity * 100))
    except Exception:
        match_score = 0

    resume_skills = set(_extract_keywords(resume_text))
    jd_skills     = set(_extract_keywords(jd_text))

    matched_skills = sorted(resume_skills & jd_skills)
    missing_skills = sorted(jd_skills - resume_skills)
    common_keywords = sorted(matched_skills)

    if match_score >= 70:
        recommendation = "Strong match — you meet most of the job requirements."
    elif match_score >= 45:
        recommendation = "Moderate match — consider adding missing skills to improve fit."
    else:
        recommendation = "Low match — significant gaps exist between your resume and the JD."

    return {
        "match_score":      match_score,
        "matched_skills":   matched_skills,
        "missing_skills":   missing_skills,
        "common_keywords":  common_keywords,
        "recommendation":   recommendation,
    }
