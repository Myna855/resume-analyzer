from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_margins(20, 20, 20)

# Name
pdf.set_font("Helvetica", "B", 22)
pdf.cell(0, 10, "John Doe", ln=True, align="C")

# Contact
pdf.set_font("Helvetica", "", 10)
pdf.cell(0, 6, "john.doe@email.com  |  +91 9876543210  |  github.com/johndoe", ln=True, align="C")
pdf.ln(4)

def section(title):
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_fill_color(230, 230, 230)
    pdf.cell(0, 8, title, ln=True, fill=True)
    pdf.ln(1)

def body(text):
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6, text)
    pdf.ln(1)

# Summary
section("SUMMARY")
body("Final year B.Tech Computer Science student with 1 year of internship experience in Python and web development. Passionate about building scalable applications and solving real-world problems using technology.")

# Skills
section("SKILLS")
body("Programming Languages: Python, Java, JavaScript, C++\nWeb Technologies: React, Django, Flask, HTML, CSS, Node.js\nDatabases: MySQL, PostgreSQL, MongoDB\nTools & Cloud: Git, Docker, AWS, Linux\nData Science: Machine Learning, Pandas, NumPy, Scikit-learn")

# Experience
section("EXPERIENCE")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 6, "Software Development Intern - TechCorp Solutions", ln=True)
pdf.set_font("Helvetica", "I", 9)
pdf.cell(0, 5, "June 2023 - June 2024", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.multi_cell(0, 6, "- Developed and deployed REST APIs using Django and PostgreSQL\n- Built React frontend for internal dashboard, improving team productivity by 40%\n- Automated data pipeline reducing manual effort by 60%\n- Collaborated with a team of 5 engineers using Agile and Scrum methodology")
pdf.ln(2)

# Projects
section("PROJECTS")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 6, "Resume Analyzer CLI Tool", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.multi_cell(0, 6, "Built a Python CLI tool that analyzes resumes using NLP and rule-based scoring. Features include skill extraction, ATS scoring, and job description matching using TF-IDF.")
pdf.ln(2)
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 6, "E-Commerce Web Application", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.multi_cell(0, 6, "Developed a full-stack e-commerce platform using React and Django REST Framework with JWT authentication and Stripe payment integration.")
pdf.ln(2)

# Education
section("EDUCATION")
pdf.set_font("Helvetica", "B", 10)
pdf.cell(0, 6, "B.Tech Computer Science - XYZ University", ln=True)
pdf.set_font("Helvetica", "", 10)
pdf.cell(0, 5, "2021 - 2025  |  CGPA: 8.4/10", ln=True)
pdf.ln(2)

# Certifications
section("CERTIFICATIONS")
body("- Python for Data Science - Coursera (2023)\n- AWS Cloud Practitioner - Amazon (2024)\n- Machine Learning Specialization - Andrew Ng, Coursera (2024)")

pdf.output("john_resume.pdf")
print("Created: john_resume.pdf")
