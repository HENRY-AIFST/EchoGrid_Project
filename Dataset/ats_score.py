def calculate_ats_score(user_skills, required_skills):

    user_skills = [s.lower() for s in user_skills]
    required_skills = [s.lower() for s in required_skills]

    matched = set(user_skills) & set(required_skills)

    if len(required_skills) == 0:
        return 0

    score = (len(matched) / len(required_skills)) * 100

    return round(score, 2)
