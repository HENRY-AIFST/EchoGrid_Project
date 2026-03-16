import re


def _normalize_text(text):
    return re.sub(r"\s+", " ", text.lower()).strip()


def _extract_user_skills(resume_text, job_skills):
    clean_text = _normalize_text(resume_text)
    detected = []
    for skill in job_skills:
        if skill.lower() in clean_text:
            detected.append(skill.lower())
    return sorted(set(detected))


def _calculate_ats_score(user_skills, job_skills):
    if not job_skills:
        return 0
    matched = len(set(user_skills))
    total = len(set(s.lower() for s in job_skills))
    if total == 0:
        return 0
    return round((matched / total) * 100)


def _generate_learning_path(missing_skills):
    return [f"Learn {skill.title()} through structured tutorials and build one project" for skill in missing_skills]


def analyze_resume(resume_text, job_skills):
    normalized_job_skills = [skill.lower() for skill in job_skills]
    user_skills = _extract_user_skills(resume_text, normalized_job_skills)
    skill_gap = [skill for skill in normalized_job_skills if skill not in user_skills]
    ats_score = _calculate_ats_score(user_skills, normalized_job_skills)

    return {
        "ats_score": ats_score,
        "user_skills": user_skills,
        "skill_gap": skill_gap,
        "learning_path": _generate_learning_path(skill_gap),
    }
