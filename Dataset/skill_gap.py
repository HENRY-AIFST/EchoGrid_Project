import pandas as pd

df = pd.read_csv("skills_dataset.csv")

def get_required_skills(job_role):
    return df[df["job_role"] == job_role]["skill"].tolist()

def find_skill_gap(user_skills, job_role):
    required = get_required_skills(job_role)
    missing = list(set(required) - set(user_skills))
    return missing

user_skills = ["Python", "SQL"]
target_job = "Data Scientist"

missing = find_skill_gap(user_skills, target_job)

print("Missing Skills:", missing)
