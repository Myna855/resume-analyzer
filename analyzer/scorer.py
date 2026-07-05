import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from data.skills import ACTION_VERBS

try:
    import textstat
    _TEXTSTAT_AVAILABLE = True
except ImportError:
    _TEXTSTAT_AVAILABLE = False

MAX_SCORES = {
    "Section Completeness": 25,
    "Skills Count":         20,
    "Contact Info":         10,
    "Resume Length":        15,
    "Readability":          15,
    "Action Verbs":         15,
}

STATIC_ATS_TIPS = [
    "Use standard section headings like 'Experience', 'Education', 'Skills'.",
    "Avoid tables, text boxes, and columns — ATS parsers may miss them.",
    "Save and submit your resume as a .pdf or .docx file.",
    "Include the job title in your resume if it matches the role.",
    "Spell out abbreviations at least once (e.g., 'Machine Learning (ML)').",
]


def _score_sections(sections: list) -> tuple[int, list, list]:
    all_sections = ["summary", "skills", "experience", "education", "projects", "certifications"]
    found = set(sections)
    score = min(len(found), 5) * 5  # 5 pts per section, max 25
    missing = [s.title() for s in all_sections if s not in found]
    present = [s.title() for s in all_sections if s in found]
    return score, present, missing


def _score_skills(skills: list) -> int:
    n = len(skills)
    if n >= 16:
        return 20
    elif n >= 11:
        return 15
    elif n >= 6:
        return 10
    elif n >= 1:
        return 5
    return 0


def _score_contact(email, phone) -> int:
    return (5 if email else 0) + (5 if phone else 0)


def _score_length(word_count: int) -> int:
    if 300 <= word_count <= 700:
        return 15
    elif 200 <= word_count < 300 or 700 < word_count <= 1000:
        return 10
    elif word_count > 1000:
        return 5
    return 3


def _score_readability(text: str) -> int:
    if not _TEXTSTAT_AVAILABLE:
        return 8  # default mid score
    score = textstat.flesch_reading_ease(text)
    # Flesch: 60-70 is ideal for professional writing
    if 50 <= score <= 80:
        return 15
    elif 30 <= score < 50 or 80 < score <= 90:
        return 10
    elif 10 <= score < 30:
        return 5
    return 3


def _score_action_verbs(text: str) -> int:
    lower = text.lower()
    count = sum(1 for v in ACTION_VERBS if re.search(r"\b" + v + r"\b", lower))
    if count >= 10:
        return 15
    elif count >= 6:
        return 10
    elif count >= 3:
        return 7
    elif count >= 1:
        return 4
    return 0


def score_resume(text: str, extracted: dict) -> dict:
    sec_score, present_sections, missing_sections = _score_sections(extracted["sections_detected"])
    skills_score   = _score_skills(extracted["skills"])
    contact_score  = _score_contact(extracted["email"], extracted["phone"])
    length_score   = _score_length(extracted["word_count"])
    read_score     = _score_readability(text)
    verb_score     = _score_action_verbs(text)

    breakdown = {
        "Section Completeness": sec_score,
        "Skills Count":         skills_score,
        "Contact Info":         contact_score,
        "Resume Length":        length_score,
        "Readability":          read_score,
        "Action Verbs":         verb_score,
    }
    overall = sum(breakdown.values())

    return {
        "overall_score":      overall,
        "breakdown":          breakdown,
        "max_scores":         MAX_SCORES,
        "present_sections":   present_sections,
        "missing_sections":   missing_sections,
    }


def generate_feedback(text: str, extracted: dict, scores: dict) -> dict:
    strengths, weaknesses, suggestions = [], [], []

    # Strengths
    if scores["overall_score"] >= 70:
        strengths.append("Well-structured resume with a strong overall score.")
    if len(extracted["skills"]) >= 10:
        strengths.append(f"Strong skill set with {len(extracted['skills'])} skills detected.")
    if extracted["email"] and extracted["phone"]:
        strengths.append("Complete contact information provided.")
    if scores["breakdown"]["Action Verbs"] >= 10:
        strengths.append("Good use of action verbs to describe achievements.")
    if scores["breakdown"]["Resume Length"] == 15:
        strengths.append(f"Ideal resume length ({extracted['word_count']} words).")
    if extracted["years_of_experience"] > 0:
        strengths.append(f"Detected ~{extracted['years_of_experience']} years of experience.")

    # Weaknesses
    if scores["missing_sections"]:
        weaknesses.append(f"Missing sections: {', '.join(scores['missing_sections'])}.")
    if len(extracted["skills"]) < 6:
        weaknesses.append("Too few skills listed — add more relevant technical skills.")
    if not extracted["email"]:
        weaknesses.append("No email address found.")
    if not extracted["phone"]:
        weaknesses.append("No phone number found.")
    if scores["breakdown"]["Action Verbs"] < 5:
        weaknesses.append("Very few action verbs used — makes the resume less impactful.")
    if extracted["word_count"] < 200:
        weaknesses.append("Resume is too short — add more detail to your experience.")
    if extracted["word_count"] > 1000:
        weaknesses.append("Resume may be too long — try to keep it under 1000 words.")

    # Suggestions
    if "summary" not in extracted["sections_detected"]:
        suggestions.append("Add a 2–3 sentence professional summary at the top.")
    if "projects" not in extracted["sections_detected"]:
        suggestions.append("Add a Projects section to showcase hands-on work.")
    if len(extracted["skills"]) < 10:
        suggestions.append("List more specific technical skills relevant to your target role.")
    if scores["breakdown"]["Action Verbs"] < 7:
        suggestions.append("Start bullet points with strong action verbs (e.g., Led, Built, Improved).")
    suggestions.append("Quantify achievements where possible (e.g., 'Improved performance by 30%').")
    if "certifications" not in extracted["sections_detected"]:
        suggestions.append("Add relevant certifications or online courses to boost credibility.")

    # Dynamic ATS tips
    ats_tips = list(STATIC_ATS_TIPS[:3])
    if scores["missing_sections"]:
        ats_tips.append(f"Add missing sections: {', '.join(scores['missing_sections'][:2])} — ATS expects them.")
    if len(extracted["skills"]) < 8:
        ats_tips.append("Include more keywords from the job description to improve ATS matching.")

    return {
        "strengths":   strengths[:5],
        "weaknesses":  weaknesses[:5],
        "suggestions": suggestions[:6],
        "ats_tips":    ats_tips[:5],
    }
