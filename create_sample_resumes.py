from fpdf import FPDF

def create_resume(filename, name, email, phone, summary, skills_text,
                  experiences, projects, education, certifications):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(20, 20, 20)

    # Name
    pdf.set_font("Helvetica", "B", 22)
    pdf.cell(0, 10, name, ln=True, align="C")

    # Contact
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"{email}  |  {phone}", ln=True, align="C")
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

    section("SUMMARY")
    body(summary)

    section("SKILLS")
    body(skills_text)

    section("EXPERIENCE")
    for exp in experiences:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 6, exp["title"], ln=True)
        pdf.set_font("Helvetica", "I", 9)
        pdf.cell(0, 5, exp["duration"], ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, exp["desc"])
        pdf.ln(2)

    section("PROJECTS")
    for proj in projects:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 6, proj["title"], ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.multi_cell(0, 6, proj["desc"])
        pdf.ln(2)

    section("EDUCATION")
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, education["degree"], ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 5, education["year"], ln=True)
    pdf.ln(2)

    section("CERTIFICATIONS")
    body(certifications)

    pdf.output(filename)
    print(f"Created: {filename}")


# ── Resume 1: Data Science ──────────────────────────────────────────────────
create_resume(
    filename="priya_data_scientist.pdf",
    name="Priya Sharma",
    email="priya.sharma@email.com",
    phone="+91 9123456780",
    summary="Aspiring Data Scientist with strong background in statistics, machine learning, and data visualization. Experienced in building predictive models and deriving actionable insights from large datasets.",
    skills_text="Programming: Python, R, SQL\nML Libraries: Scikit-learn, TensorFlow, Keras, XGBoost\nData Tools: Pandas, NumPy, Matplotlib, Seaborn, Tableau, Power BI\nDatabases: MySQL, PostgreSQL, MongoDB\nOther: Git, Jupyter Notebook, Google Colab, Excel",
    experiences=[
        {
            "title": "Data Science Intern - Analytics Corp",
            "duration": "Jan 2024 - June 2024",
            "desc": "- Built customer churn prediction model using Random Forest achieving 87% accuracy\n- Performed EDA on 500K+ records to identify key sales trends\n- Created interactive dashboards in Tableau for business stakeholders\n- Automated weekly reporting pipeline saving 5 hours per week"
        }
    ],
    projects=[
        {
            "title": "House Price Prediction",
            "desc": "Developed a regression model using XGBoost to predict house prices with RMSE of 0.12. Applied feature engineering and hyperparameter tuning."
        },
        {
            "title": "Sentiment Analysis on Twitter Data",
            "desc": "Built an NLP pipeline using NLTK and Scikit-learn to classify tweets as positive, negative or neutral with 83% accuracy."
        }
    ],
    education={"degree": "B.Tech Computer Science - ABC University", "year": "2021 - 2025  |  CGPA: 8.9/10"},
    certifications="- IBM Data Science Professional Certificate - Coursera (2023)\n- Google Data Analytics Certificate (2024)\n- Deep Learning Specialization - Andrew Ng (2024)"
)

# ── Resume 2: Frontend Developer ────────────────────────────────────────────
create_resume(
    filename="rahul_frontend_dev.pdf",
    name="Rahul Verma",
    email="rahul.verma@email.com",
    phone="+91 9988776655",
    summary="Creative Frontend Developer with expertise in React and modern JavaScript. Passionate about building responsive, accessible, and visually appealing web applications with great user experience.",
    skills_text="Languages: HTML, CSS, JavaScript, TypeScript\nFrameworks: React, Next.js, Vue.js, Tailwind CSS, Bootstrap\nTools: Git, Webpack, Vite, Figma, Adobe XD\nTesting: Jest, Cypress\nOther: REST APIs, GraphQL, Firebase",
    experiences=[
        {
            "title": "Frontend Developer Intern - WebStudio Pvt Ltd",
            "duration": "July 2023 - Jan 2024",
            "desc": "- Developed 10+ responsive web pages using React and Tailwind CSS\n- Improved website load time by 40% through code splitting and lazy loading\n- Integrated REST APIs and handled state management using Redux\n- Collaborated with designers to convert Figma mockups into pixel-perfect UI"
        }
    ],
    projects=[
        {
            "title": "Portfolio Website Builder",
            "desc": "Built a drag-and-drop portfolio website builder using React and Firebase. Users can create and publish their portfolio in minutes."
        },
        {
            "title": "Weather Dashboard App",
            "desc": "Created a real-time weather app using React and OpenWeatherMap API with location-based search and 5-day forecast charts using Chart.js."
        }
    ],
    education={"degree": "B.Tech Information Technology - DEF University", "year": "2020 - 2024  |  CGPA: 7.8/10"},
    certifications="- Meta Frontend Developer Certificate - Coursera (2023)\n- JavaScript Algorithms and Data Structures - freeCodeCamp (2022)\n- Responsive Web Design - freeCodeCamp (2022)"
)

# ── Resume 3: DevOps Engineer ───────────────────────────────────────────────
create_resume(
    filename="arjun_devops.pdf",
    name="Arjun Nair",
    email="arjun.nair@email.com",
    phone="+91 8877665544",
    summary="DevOps Engineer with 2 years of experience in automating CI/CD pipelines, managing cloud infrastructure, and improving deployment reliability. Skilled in AWS, Docker, and Kubernetes.",
    skills_text="Cloud: AWS, Azure, Google Cloud\nContainerization: Docker, Kubernetes, Helm\nCI/CD: Jenkins, GitHub Actions, GitLab CI\nIaC: Terraform, Ansible, CloudFormation\nMonitoring: Prometheus, Grafana, ELK Stack\nScripting: Bash, Python\nOther: Linux, Git, Nginx",
    experiences=[
        {
            "title": "DevOps Engineer - CloudTech Solutions",
            "duration": "2022 - 2024",
            "desc": "- Designed and maintained CI/CD pipelines using Jenkins reducing deployment time by 60%\n- Migrated 15 microservices to Kubernetes on AWS EKS\n- Automated infrastructure provisioning using Terraform saving 10 hours per week\n- Set up monitoring and alerting using Prometheus and Grafana"
        }
    ],
    projects=[
        {
            "title": "Automated Deployment Pipeline",
            "desc": "Built a fully automated CI/CD pipeline using GitHub Actions, Docker, and AWS ECS that deploys applications on every push to main branch."
        },
        {
            "title": "Infrastructure as Code Setup",
            "desc": "Created reusable Terraform modules for provisioning AWS VPC, EC2, RDS, and S3 resources used across multiple projects."
        }
    ],
    education={"degree": "B.E. Computer Engineering - GHI University", "year": "2018 - 2022  |  CGPA: 7.5/10"},
    certifications="- AWS Certified Solutions Architect - Associate (2023)\n- Certified Kubernetes Administrator - CNCF (2023)\n- HashiCorp Certified Terraform Associate (2024)"
)

# ── Resume 4: Android Developer ─────────────────────────────────────────────
create_resume(
    filename="sneha_android_dev.pdf",
    name="Sneha Patel",
    email="sneha.patel@email.com",
    phone="+91 7766554433",
    summary="Android Developer with experience building user-friendly mobile applications using Kotlin and Java. Strong understanding of Material Design, RESTful APIs, and mobile performance optimization.",
    skills_text="Languages: Kotlin, Java, XML\nAndroid: Android SDK, Jetpack Compose, MVVM, Room DB, Retrofit\nTools: Android Studio, Git, Firebase, Postman\nTesting: JUnit, Espresso\nOther: REST APIs, SQLite, Push Notifications, Google Maps API",
    experiences=[
        {
            "title": "Android Developer Intern - MobileApps India",
            "duration": "Feb 2024 - Aug 2024",
            "desc": "- Developed 3 Android apps published on Google Play Store with 10K+ downloads\n- Implemented MVVM architecture improving code maintainability\n- Integrated Firebase for real-time database, authentication and push notifications\n- Reduced app crash rate by 35% through thorough testing and debugging"
        }
    ],
    projects=[
        {
            "title": "Food Delivery App",
            "desc": "Built a food delivery Android app using Kotlin with features like real-time order tracking, Google Maps integration, and Razorpay payment gateway."
        },
        {
            "title": "Expense Tracker App",
            "desc": "Developed a personal finance tracker using Kotlin and Room database with charts for monthly spending analysis using MPAndroidChart."
        }
    ],
    education={"degree": "B.Tech Computer Science - JKL University", "year": "2020 - 2024  |  CGPA: 8.2/10"},
    certifications="- Associate Android Developer - Google (2023)\n- Kotlin for Android Developers - Udemy (2022)\n- Firebase in a Weekend - Google (2023)"
)

print("\nAll 4 resumes created successfully!")
print("Run: python3 main.py priya_data_scientist.pdf")
print("Run: python3 main.py rahul_frontend_dev.pdf")
print("Run: python3 main.py arjun_devops.pdf")
print("Run: python3 main.py sneha_android_dev.pdf")
