def generate_learning_path(missing_skills):

    roadmap = []

    for skill in missing_skills:

        roadmap.append({
            "skill": skill,
            "action": f"Learn {skill}",
            "resource": f"Search '{skill}' on Coursera, YouTube, or Udemy"
        })

    return roadmap
