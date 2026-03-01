# 🚀 AI-Powered Skill Gap Visualizer & Learning Path Generator

An intelligent web-based system that analyzes a user's current skills and compares them with industry job requirements to identify skill gaps and generate a personalized learning roadmap.

---

## 📌 Project Overview

In today’s rapidly evolving job market, students and early-career professionals often struggle to understand:

- What skills they currently have
- What skills are required for their desired job role
- What skills they are missing
- How to follow a structured and goal-oriented learning path

This project uses AI and NLP techniques to provide a data-driven solution for career planning.

---

## 🎯 Objectives

- Extract user skills from resume or manual input  
- Compare user skills with industry job requirements  
- Identify missing skills (Skill Gaps)  
- Calculate Skill Match Percentage  
- Generate Personalized Learning Roadmap  
- Visualize skill readiness through dashboard  

---

## 🛠 Tech Stack

### 🔹 Backend
- Python
- Flask

### 🔹 Frontend
- HTML
- CSS
- JavaScript
- Bootstrap / Tailwind CSS

### 🔹 Database
- MongoDB / SQLite

### 🔹 Libraries & Tools
- spaCy / NLTK (NLP Processing)
- Chart.js (Data Visualization)
- Flask-Login (Authentication)
- PyPDF2 (Resume Parsing - Optional)

---

## 🏗 System Architecture

1. User Authentication Module  
2. Resume Upload / Manual Skill Input  
3. NLP-based Skill Extraction  
4. Job Role Requirement Mapping  
5. Skill Gap Analysis Engine  
6. Learning Path Generator  
7. Interactive Dashboard  
8. Progress Tracking System  

---

## ⚙️ Working Principle

### Step 1: User Login / Register
Secure authentication system with password hashing.

### Step 2: Skill Input
- Resume upload (PDF/Text), OR  
- Manual skill entry  

### Step 3: NLP Skill Extraction
System extracts:
- Technical skills  
- Tools  
- Technologies  

### Step 4: Skill Comparison
System compares:

User Skills vs Required Skills

Skill Match Formula:

Skill Match % = (Matched Skills / Total Required Skills) × 100

### Step 5: Learning Path Generation
Missing skills are structured into:

- Beginner Level  
- Intermediate Level  
- Advanced Level  

Recommended:
- Projects  
- Tools to practice  
- Learning suggestions  

### Step 6: Dashboard Visualization
Displays:
- Skill Match Percentage  
- Missing Skills  
- Recommended Skills  
- Progress Graph  

---

## 📊 Example

Target Role: Data Scientist  

User Skills:
- Python
- Statistics

Required Skills:
- Python
- Statistics
- SQL
- Machine Learning
- Data Visualization

Output:
- Missing Skills → SQL, Machine Learning, Data Visualization  
- Skill Match → 40%  
- Learning Path → SQL → ML → Projects  

---

## 📂 Project Structure
skill-gap-analyzer/
│
├── app.py
├── models.py
├── requirements.txt
├── database.db
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│
├── static/
│ ├── css/
│ ├── js/
│
└── README.md

---

## ▶️ Installation Guide

### 1️⃣ Clone Repository

---git clone https://github.com/your-username/skill-gap-analyzer.git
cd skill-gap-analyzer


Open browser:http://127.0.0.1:5000/


## 🔐 Security Features

- Password Hashing  
- Session Management  
- Secure User Authentication  
- Protected Routes  

---

## 📈 Future Enhancements

- LinkedIn API Integration  
- Real-time Job Market Analysis  
- AI-based Skill Importance Ranking  
- Course Recommendation API  
- Resume PDF Auto Parsing  
- ML-based Recommendation Engine  

---

## 👨‍💻 Developed By

- Pranjal Dutta  
- Rahul Breeds  
- Reena Fogat  
- Utkarsh Thapliyal  

Department of Computer Science Engineering  

---

## 📜 License

This project is developed for academic and educational purposes only.

