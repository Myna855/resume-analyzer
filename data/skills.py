SKILLS = {
    "Programming Languages": [
        "python", "java", "javascript", "typescript", "c", "c++", "c#", "ruby",
        "php", "swift", "kotlin", "go", "golang", "rust", "scala", "r",
        "matlab", "perl", "bash", "shell", "powershell", "vba", "dart", "lua",
        "haskell", "groovy", "objective-c", "assembly",
    ],
    "Web Technologies": [
        "html", "css", "react", "reactjs", "angular", "angularjs", "vue",
        "vuejs", "nodejs", "node.js", "express", "expressjs", "django",
        "flask", "fastapi", "spring", "spring boot", "asp.net", "laravel",
        "rails", "ruby on rails", "next.js", "nextjs", "nuxt", "gatsby",
        "jquery", "bootstrap", "tailwind", "tailwindcss", "sass", "less",
        "webpack", "vite", "graphql", "rest", "restful", "soap", "websocket",
        "redux", "mobx", "svelte",
    ],
    "Databases": [
        "sql", "mysql", "postgresql", "postgres", "sqlite", "oracle",
        "microsoft sql server", "mssql", "mongodb", "redis", "cassandra",
        "elasticsearch", "dynamodb", "firebase", "neo4j", "couchdb",
        "mariadb", "nosql", "hbase", "influxdb",
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "azure", "google cloud", "gcp",
        "docker", "kubernetes", "k8s", "jenkins", "gitlab ci", "github actions",
        "terraform", "ansible", "chef", "puppet", "vagrant", "nginx",
        "apache", "linux", "unix", "git", "github", "gitlab", "bitbucket",
        "ci/cd", "devops", "microservices", "serverless", "lambda",
        "cloudformation", "helm", "prometheus", "grafana", "elk stack",
    ],
    "Data Science & ML": [
        "machine learning", "deep learning", "artificial intelligence", "ai",
        "neural network", "nlp", "natural language processing",
        "computer vision", "data science", "data analysis", "data mining",
        "pandas", "numpy", "scipy", "scikit-learn", "sklearn", "tensorflow",
        "keras", "pytorch", "opencv", "matplotlib", "seaborn", "plotly",
        "tableau", "power bi", "excel", "statistics", "regression",
        "classification", "clustering", "random forest", "xgboost",
        "hadoop", "spark", "apache spark", "kafka", "airflow", "dbt",
        "etl", "data warehouse", "data pipeline",
    ],
    "Mobile Development": [
        "android", "ios", "react native", "flutter", "xamarin",
        "swift", "kotlin", "ionic", "cordova", "pwa",
    ],
    "Testing & QA": [
        "unit testing", "integration testing", "selenium", "cypress",
        "jest", "pytest", "junit", "mocha", "chai", "test automation",
        "manual testing", "qa", "quality assurance", "postman",
    ],
    "Soft Skills": [
        "leadership", "communication", "teamwork", "collaboration",
        "problem solving", "critical thinking", "time management",
        "project management", "agile", "scrum", "kanban", "jira",
        "presentation", "negotiation", "mentoring", "analytical",
        "adaptability", "creativity", "attention to detail",
    ],
    "Security": [
        "cybersecurity", "penetration testing", "ethical hacking",
        "network security", "cryptography", "owasp", "siem", "firewall",
        "ssl", "tls", "oauth", "jwt", "security",
    ],
    "Networking": [
        "tcp/ip", "dns", "dhcp", "vpn", "networking", "cisco",
        "routing", "switching", "load balancing", "cdn",
    ],
}

# Flat list for quick lookup
ALL_SKILLS = [skill for category in SKILLS.values() for skill in category]

ACTION_VERBS = [
    "led", "managed", "developed", "built", "designed", "implemented",
    "created", "launched", "improved", "increased", "reduced", "optimized",
    "delivered", "achieved", "collaborated", "coordinated", "mentored",
    "trained", "analyzed", "researched", "wrote", "deployed", "maintained",
    "automated", "streamlined", "integrated", "architected", "established",
    "spearheaded", "executed", "transformed", "scaled", "migrated",
    "refactored", "debugged", "tested", "reviewed", "published",
    "presented", "negotiated", "secured", "resolved", "supported",
    "enhanced", "engineered", "configured", "monitored", "documented",
]
