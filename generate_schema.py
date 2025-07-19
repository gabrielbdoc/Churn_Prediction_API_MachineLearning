import joblib

columns = joblib.load("models/columns.pkl")

print("from pydantic import BaseModel\n\nclass CustomerData(BaseModel):")
for col in columns:
    print(f"    {col}: float")