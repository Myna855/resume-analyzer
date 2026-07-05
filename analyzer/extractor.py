import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from data.skills import SKILLS, ALL_SKILLS

try:
    import spacy
    _nlp = spacy.load("en_core_web_sm")
    _SPACY_AVAILABLE = True
except Exception:
    _SPACY_AVAILABLE = False

SECTION_HEADERS = {
    "summary":        ["summary", "objective", "profile", "about me", "about", "career objective"],
    "skills":         ["skills", "technical skills", "technologies", "competencies", "expertise"],
    "experience":     ["experience", "work experience", "employment", "work history", "professional experience"],
    "education":      ["education", "academic", "qualifications", "academic background"],
    "projects":       ["projects", "personal projects", "academic projects", "portfolio"],
    "certifications": ["certifications", "certificates", "awards", "achievements", "honors"],
}

DEGREE_PATTERNS = [
    r"\b(b\.?tech|b\.?e\.?|b\.?sc|bachelor|b\.?a\.?|bca|bba)\b",
    r"\b(m\.?tech|m\.?e\.?|m\.?sc|master|mba|mca|m\.?a\.?)\b",
    r"\b(phd|ph\.?d|doctorate|doctor)\b",
    r"\b(diploma|hsc|ssc|10th|12th|intermediate)\b",
]


def _find_email(text: str) -> str:
    matches = re.findall(r"[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}", text)
    return matches[0] if matches else None


def _find_phone(text: str) -> str:
    patterns = [
        r"\+?\d[\d\s\-().]{8,14}\d",
        r"\b\d{10}\b",
        r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group().strip()
    return None


def _find_name(text: str) -> str:
    if _SPACY_AVAILABLE:
        # Check first 500 chars — name is usually at the top
        doc = _nlp(text[:500])
        for ent in doc.ents:
            if ent.label_ == "PERSON" and len(ent.text.split()) >= 2:
                return ent.text.strip()

    # Fallback: first non-empty line that looks like a name
    for line in text.splitlines()[:8]:
        line = line.strip()
        if (
            2 <= len(line.split()) <= 4
            and not re.search(r"[@|/\\|0-9]", line)
            and not any(kw in line.lower() for kw in ["resume", "cv", "curriculum"])
        ):
            return line
    return None


def _find_skills(text: str) -> dict:
    lower = text.lower()
    matched_by_category = {}
    for category, skills in SKILLS.items():
        found = []
        for skill in skills:
            # word boundary match to avoid partial matches
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, lower):
                found.append(skill)
        if found:
            matched_by_category[category] = found
    return matched_by_category


def _detect_sections(text: str) -> list:
    lower = text.lower()
    found = []
    for section, keywords in SECTION_HEADERS.items():
        for kw in keywords:
            if re.search(r"\b" + re.escape(kw) + r"\b", lower):
                found.append(section)
                break
    return found


def _find_education(text: str) -> list:
    education = []
    for pat in DEGREE_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            start = max(0, m.start() - 10)
            end = min(len(text), m.end() + 120)
            snippet = text[start:end].strip().replace("\n", " ")
            education.append(snippet)
    return education[:5]  # cap at 5


def _estimate_years_experience(text: str) -> float:
    # Match patterns like "2019 - 2022", "Jan 2020 – Present", "3 years"
    year_range_pat = r"(20\d{2}|19\d{2})\s*[-–—to]+\s*(20\d{2}|19\d{2}|present|current)"
    total = 0.0
    import datetime
    current_year = datetime.datetime.now().year

    for m in re.finditer(year_range_pat, text, re.IGNORECASE):
        try:
            start_yr = int(m.group(1))
            end_str = m.group(2).lower()
            end_yr = current_year if end_str in ("present", "current") else int(end_str)
            diff = end_yr - start_yr
            if 0 < diff <= 50:
                total += diff
        except ValueError:
            continue

    # Also look for "X years of experience"
    yr_match = re.search(r"(\d+)\+?\s*years?\s*(of\s*)?experience", text, re.IGNORECASE)
    if yr_match and total == 0:
        total = float(yr_match.group(1))

    return round(total, 1)


def extract_info(text: str) -> dict:
    skills_by_category = _find_skills(text)
    all_found_skills = [s for skills in skills_by_category.values() for s in skills]

    return {
        "name":                _find_name(text),
        "email":               _find_email(text),
        "phone":               _find_phone(text),
        "skills_by_category":  skills_by_category,
        "skills":              all_found_skills,
        "sections_detected":   _detect_sections(text),
        "education_snippets":  _find_education(text),
        "years_of_experience": _estimate_years_experience(text),
        "word_count":          len(text.split()),
    }
