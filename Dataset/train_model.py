import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("skills_dataset.csv")

# Group skills by job role
grouped = df.groupby("job_role")["skill"].apply(list).reset_index()

# Convert skills into binary features
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(grouped["skill"])

y = grouped["job_role"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("skill_model.pkl", "wb"))
pickle.dump(mlb, open("skill_encoder.pkl", "wb"))

print("Model trained successfully")

