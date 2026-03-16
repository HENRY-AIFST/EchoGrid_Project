import pickle

# Load trained model
model = pickle.load(open("skill_model.pkl", "rb"))
mlb = pickle.load(open("skill_encoder.pkl", "rb"))

# Example user skills
user_skills = [["Python", "SQL", "Machine Learning"]]

# Convert skills to ML format
X = mlb.transform(user_skills)

# Predict job
prediction = model.predict(X)

print("Predicted Job Role:", prediction[0])

